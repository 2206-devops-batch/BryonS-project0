import pathlib
import json

root_path = pathlib.Path.cwd()
snapshot_dir_path = root_path.joinpath('snapshot')
snapshot_file_path = snapshot_dir_path.joinpath('github_data.json')

def createSnapshotData(data):
    with open(snapshot_file_path, 'w') as f:
        json.dumps(data, f)


def readFile(path):
    try:
        with open(path) as f:
           return json.loads(f)
    except:
        return []


# load github db info or create if not exist.
def get_database():
    #check if directory exist
    if not snapshot_dir_path.exists():
        print('Created GitHub backup directory: ' + str(snapshot_dir_path))
        snapshot_dir_path.mkdir()
    
    return readFile(snapshot_file_path)
