import pathlib, json


SNAPSHOT_DIR =  pathlib.Path.cwd().joinpath('snapshot')
GITHUB_DB_FILE_PATH = SNAPSHOT_DIR.joinpath('github_data.json')

# if file does not exist, create it.
def read_file(path):
        if not path.exists():
            return []
        else:
            with open(path) as f:
                return json.load(f)


# load github db info or create if not exist.
def get_database():
    #check if directory exist
    if not SNAPSHOT_DIR.exists():
        print('Created GitHub backup directory: ' + str(SNAPSHOT_DIR))
        SNAPSHOT_DIR.mkdir()
    
    return read_file(GITHUB_DB_FILE_PATH)
