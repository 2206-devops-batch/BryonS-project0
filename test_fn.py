
import pathlib, json
import unittest
# from unittest import mock
# from unittest.mock import patch

from lib.fetch_github_repo import create_file_name
from lib import github_cred
from lib.snapshot import GITHUB_DB_FILE_PATH, SNAPSHOT_DIR

class Test_Snapshot(unittest.TestCase):
    # setup once before running test.
    @classmethod
    def setUpClass(cls):
        unit_test_dir = pathlib.Path.cwd().joinpath('unit_test')
        db_file = unit_test_dir.joinpath('dummy_data1.json')
        data_file = unit_test_dir.joinpath('dummy_data2.json')
        db_json = db_file.read_bytes()
        data_json = data_file.read_bytes()
        # set as a class attribute
        cls.db = json.loads(db_json)
        cls.data = json.loads(data_json)

        
    
    def test_create_file_name(self):
        self.assertEqual(create_file_name("Bob", 1234567890), "Bob_1234567890.zip")
        self.assertEqual(create_file_name(" Bob ", " 1234567890 "), "Bob_1234567890.zip")
        self.assertEqual(create_file_name("Bob ", 1234567890.009), "Bob_1234567890.009.zip")



if __name__ == '__main__':
    unittest.main()
