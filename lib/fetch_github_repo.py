import requests, json 
from datetime import datetime
from lib.snapshot import SNAPSHOT_DIR, GITHUB_DB_FILE_PATH


def filter_data(data):
    db = []
    for d in data:
        obj = {
            "name": d['name'], # name of repo
            "default_branch": d['default_branch'], # master, main ..
            "updated_at": datetime.strptime(d['updated_at'], "%Y-%m-%dT%H:%M:%SZ").timestamp(),
            "pushed_at": datetime.strptime(d['pushed_at'], "%Y-%m-%dT%H:%M:%SZ").timestamp()
        }
        db.append(obj)
    return db


# both args are list of dicts. Keys: name, default_branch, updated_at, pushed_at
def process_links(db, data):
    new_database = []
    download = []
    remove_list = []
    
    # get list of names
    names_list = [x['name'] for x in db]

    for new_data in data: #loop downloaded data
        # no matter what add repo to new_database
        new_database.append(new_data)
        # check if repo name is in database.
        if new_data['name'] not in names_list:
            download.append(new_data)
        else:
            for old_data in db: # name was found in database, loop database data to find change.
                # find database repo and compare
                if new_data['name'] == old_data['name']:
                    # exact match?
                    if new_data == old_data:
                        # do nothing, repo downloaded and new_data already in new_database
                        break
                    # objects didn't match, delete old and download new.
                    else:
                        remove_list.append(old_data)
                        download.append(new_data)

    print(f'You have {len(new_database)} repositories.')
    GITHUB_DB_FILE_PATH.write_text(json.dumps(new_database))
    return (download, remove_list)



def download_repo(user, name, token, default_branch, write_path):
    URL = f'https://github.com/{user}/{name}/archive/refs/heads/{default_branch}.zip'
    headers = {'Accept': 'application/vnd.github.v3+json'}
    res = requests.get(URL, auth=(user, token), headers = headers)
    with open(write_path, 'wb') as b:
        b.write(res.content)

def create_file_name(name, pushed_at):
     return f"{name}_{str(pushed_at)}.zip"

def remove_files(remove_list):
    print('\n')
    for d in remove_list:
        print(f"\t-- {create_file_name(d['name'], d['pushed_at'])}")
    remove_old_files = input('You have newer files in the repo. Would you like to remove the old repo files? (y/n) ')
    if remove_old_files == 'y' or remove_old_files == 'yes':
        for d in remove_list:
            file_name = create_file_name(d['name'], d['pushed_at'])
            try:
                SNAPSHOT_DIR.joinpath(file_name).unlink()
                print(f'Removed {file_name}')
            except:
                print(f"Couldn't delete file {file_name}" )
        print('\n')

# main entry point
def get_repositories(user, token, db):
    #Get all repos, including private and collaborator in another organization.
    URL_ALL_REPOS = 'https://api.github.com/user/repos?per_page=100&affiliation=owner,collaborator' 
    headers = {'Accept': 'application/vnd.github.v3+json'}
    res = requests.get(URL_ALL_REPOS, auth=(user, token), headers = headers)
    code = res.status_code
   
    if code > 304:
        print(f'Request failed with code: {code}')
        return

    data = res.json()

    # extract needed repo: name, updated_at, pushed_at, default_branch from GitHub response
    db_data = filter_data(data)
    download, remove_list = process_links(db, db_data)

    if download or remove_list:
        # ask to remove old repos?
        if remove_list:
           remove_files(remove_list)
        
        if download:
            print('Starting Download')
            for d in download:
                file_name = create_file_name(d['name'], d['pushed_at'])
                f_path = SNAPSHOT_DIR.joinpath(file_name)
                print(f'Downloading: {file_name}')
                download_repo(user, d['name'], token, d['default_branch'], f_path)
            print('Finished Downloading!')
    else:
        print('No changes in all repositories. Have a great day!')
