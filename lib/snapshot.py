from os import mkdir
import pathlib
import json

root_path = pathlib.Path.cwd()
snapshot_dir_path = root_path.joinpath('snapshot')
snapshot_file_path = snapshot_dir_path.joinpath('github_data.json')

#check if directory exist
def getSnapshotData():

    if not snapshot_dir_path.exists():
        print('Created GitHub backup directory: ' + str(snapshot_dir_path))
        snapshot_dir_path.mkdir()
    
    #check if github database file exist
    if not snapshot_file_path.exists():
        print('Created GitHub database file: ' + str(snapshot_file_path))
        snapshot_file_path.write_text('{}')

    # try:
    #     db = open(snapshot_file_path, mode="r+")
    # except FileNotFoundError:
    #     snapshot_file_path.touch()
