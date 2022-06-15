
import pathlib, json
import unittest
# from unittest import mock
# from unittest.mock import patch

from lib import fetch_github_repo
from lib import github_cred
from lib import snapshot

# unit_test_dir = pathlib.Path.cwd().joinpath('unit_test')
# db_file = unit_test_dir.joinpath('dummy_data1.json')
# data_file = unit_test_dir.joinpath('dummy_data2.json')

# db_json = db_file.read_bytes()
# data_json = data_file.read_bytes()

# db = json.loads(db_json)
# data = json.loads(data_json)


class TestCalc(unittest.TestCase):
    print(snapshot.snapshot_file)
  
    # def test_read_file(self):
    #     file_path = pathlib.Path.cwd().joinpath('unit_test', 'dummy_data1.json')
    #     result = snapshot.read_file()
    #     print(result)
    #     self.assertEqual(result, ('Bob', 'tuesdaymondayfriday454__34343'))

