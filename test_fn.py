
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
        # load unit test db test files and add them as class attributes.
        unit_test_dir = pathlib.Path.cwd().joinpath('unit_test')
        # set as a class attribute
        with open(unit_test_dir.joinpath('dummy_data1.json')) as f1:
            cls.db = json.load(f1)
        with open( unit_test_dir.joinpath('dummy_data2.json')) as f2:
            cls.data = json.load(f2)

        
    
    def test_create_file_name(self):
        self.assertEqual(create_file_name("Bob", 1234567890), "Bob_1234567890.zip")
        self.assertEqual(create_file_name(" Bob ", " 1234567890 "), "Bob_1234567890.zip")
        self.assertEqual(create_file_name("Bob ", 1234567890.009), "Bob_1234567890.009.zip")
        print(self.db)
        print('\n')
        print(self.data)



if __name__ == '__main__':
    unittest.main()
