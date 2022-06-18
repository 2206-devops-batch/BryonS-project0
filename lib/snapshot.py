import pathlib, json

DIR = pathlib.Path.cwd()
SNAPSHOT_DIR =  DIR.joinpath('snapshot')
GITHUB_DB_FILE_PATH = SNAPSHOT_DIR.joinpath('github_data.json')

# if file does not exist, create it.
def read_file(path):
        if not path.exists():
            return []
        else:
            with open(path) as f:
                return json.load(f)


# load github db info or create if not exist.
def get_database(DIR, FILE):
    #check if directory exist
    if not DIR.exists():
        print('Created GitHub backup directory: ' + str(DIR))
        DIR.mkdir()
    
    return read_file(FILE)
