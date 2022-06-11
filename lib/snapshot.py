import pathlib
import json

root_path = pathlib.Path.cwd()
snapshot_dir_path = root_path.joinpath('snapshot')
snapshot_file_path = snapshot_dir_path.joinpath('github_data.json')

# load github db info or create if not exist.
def database():
    #check if directory exist
    if not snapshot_dir_path.exists():
        print('Created GitHub backup directory: ' + str(snapshot_dir_path))
        snapshot_dir_path.mkdir()
    
    return readFile(snapshot_file_path)



def createSnapshotData(data):
    with open(snapshot_file_path, 'w') as f:
        json.dump(data, f)


def readFile(path):
    try:
        with open(path) as f:
           return json.load(f)
    except:
        return {}


