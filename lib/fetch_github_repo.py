import requests, json, pathlib 
from datetime import datetime

SNAPSHOT_DIR = pathlib.Path.cwd().joinpath('snapshot')

def filterData(data):
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
def processLinks(db, data):
    new_database = []
    download = []
    remove_list = []
    
    # get list of names
    names_list = []
    for d in db:
        names_list.append(d['name'])

    for new_data in data: #loop downloaded data
        # check if repo name is in database.
        if new_data['name'] not in names_list:
            download.append(new_data)
            new_database.append(new_data)
        else:
            # no matter what add repo to new_database
            new_database.append(new_data)
            for old_data in db: # loop database data
                # find database repo and compare
                if new_data['name'] == old_data['name']:
                    # exact match?
                    if new_data == old_data:
                        # do nothing, repo downloaded and new_data already in new_database
                        continue
                    # was not an exact match
                    else:
                        remove_list.append(old_data)
                        download.append(new_data)

    print(f'You have {len(new_database)} repositories.')
    SNAPSHOT_DIR.joinpath('github_data.json').write_text(json.dumps(new_database))
    return (download, remove_list)



def downloadRepo(user, name, token, default_branch, write_path):
    URL = f'https://github.com/{user}/{name}/archive/refs/heads/{default_branch}.zip'
    headers = {'Accept': 'application/vnd.github.v3+json'}
    res = requests.get(URL, auth=(user, token), headers = headers)
    # print(res.status_code)
    # h = res.headers
    # print(h)
    with open(write_path, 'wb') as b:
        b.write(res.content)



def get(user, token, db):
    #Get all repos, including private and collaborator in another organization.
    URL_ALL_REPOS = 'https://api.github.com/user/repos?per_page=100&affiliation=owner,collaborator' 

    URL = URL_ALL_REPOS
    headers = {'Accept': 'application/vnd.github.v3+json'}
    res = requests.get(URL, auth=(user, token), headers = headers)
    code = res.status_code
   
    if code > 304:
        print(f'Request failed with code: {code}')
    
    data = res.json()

    # extract needed data from repo data
    db_data = filterData(data)
    download, remove_list = processLinks(db, db_data)

    if download or remove_list:
        # ask to remove old repos?
        if remove_list:
            for d in remove_list:
                file_name = f"{d['name']}_{str(d['updated_at'])}.zip"
                print(file_name)
            remove_files = input('Would you like to remove these old repo files? (y/n)')
            if remove_files:
                for d in remove_list:
                    file_name = f"{d['name']}_{str(d['updated_at'])}.zip"
                    try:
                        SNAPSHOT_DIR.joinpath(file_name).unlink()
                        print(f'Removed {file_name}')
                    except:
                        print(f"Couldn't delete file {file_name}" )
        
        if download:
            print('Starting Download')
            for d in download:
                file_name = f"{d['name']}_{str(d['updated_at'])}.zip"
                f_path = SNAPSHOT_DIR.joinpath(file_name)
                print(f'Downloading: {file_name}')
                downloadRepo(user, d['name'], token, d['default_branch'], f_path)
            print('Finished!')
    else:
        print('No changes in all repositories. Have a great day!')

    return