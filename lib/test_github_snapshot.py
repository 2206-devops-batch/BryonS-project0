import pathlib, json
import unittest
import os, sys
# added to fix relative path import problem.
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from lib.fetch_github_repo import create_file_name, filter_data, process_links
from lib.github_cred import credentials
from lib.snapshot import get_database


DUMMY_DIR = pathlib.Path.cwd().joinpath('unittest_dummy_data')

RAW_DUMMY_GITHUB_DATA = DUMMY_DIR.joinpath('raw_dummy_github_data.json')
PROCESSED_RAW_DUMMY_GITHUB_DATA = DUMMY_DIR.joinpath('processed_raw_github_data.json')

DUMMY_OLD_DB = DUMMY_DIR.joinpath('processed_dummy_data1.json')
DUMMY_NEW_DATA = DUMMY_DIR.joinpath('processed_dummy_data2.json')

DUMMY_DOWNLOAD_DATA = DUMMY_DIR.joinpath('processed_download_data.json')
DUMMY_REMOVE_DATA = DUMMY_DIR.joinpath('processed_remove_data.json')

class Test_Snapshot(unittest.TestCase):
    def test_read_file(self):
        with open(DUMMY_OLD_DB) as f:
            TEST_DATA = json.load(f)
        self.assertEqual(get_database(DUMMY_DIR, DUMMY_OLD_DB), TEST_DATA)



class TestCredentials(unittest.TestCase):
    USER = 'Bob'
    DUMMY_PW = '3slr_KkdEJt6yr6tg7hu9045kl3df985lo43R45Fh'
    def test_credentials(self):
        self.assertEqual(credentials(self.USER, self.DUMMY_PW), (self.USER, self.DUMMY_PW))


class TestFetchGitHub(unittest.TestCase):
    USER = 'Bob'
    # setup once before running test.
    @classmethod
    def setUpClass(cls):
        with open(DUMMY_OLD_DB) as f1:
            cls.OLD_DB = json.load(f1)
        with open(DUMMY_NEW_DATA) as f2:
            cls.NEW_DATA = json.load(f2)
        # load the raw github data
        with open(RAW_DUMMY_GITHUB_DATA) as f3:
            cls.RAW_GITHUB_DATA = json.load(f3)
        # load return value after data is filtered
        with open(PROCESSED_RAW_DUMMY_GITHUB_DATA) as f4:
            cls.PROCESSED_RAW_GITHUB_DATA = json.load(f4)
        # processed download list
        with open(DUMMY_DOWNLOAD_DATA) as f5:
            cls.PROCESSED_DOWNLOAD_DATA = json.load(f5)
        # processed remove list
        with open(DUMMY_REMOVE_DATA) as f6:
            cls.PROCESSED_REMOVE_DATA = json.load(f6)

    def test_create_file_name(self):
        self.assertEqual(create_file_name(self.USER, 1234567890), f"{self.USER}_1234567890.zip")
        self.assertEqual(create_file_name(f" {self.USER} ", " 1234567890 "), f"{self.USER}_1234567890.zip")
        self.assertEqual(create_file_name(f"{self.USER} ", 1234567890.009), f"{self.USER}_1234567890.009.zip")

    def test_filter_data(self):
        self.assertEqual(filter_data(self.RAW_GITHUB_DATA), self.PROCESSED_RAW_GITHUB_DATA)

    def test_process_links(self):
        # where to write the new db dummy data.
        DUMMY_DATA_FILE_PATH = DUMMY_DIR.joinpath('temp_new_dummy_db.json')

        self.assertEqual(process_links(self.OLD_DB, self.NEW_DATA, DUMMY_DATA_FILE_PATH), (self.PROCESSED_DOWNLOAD_DATA, self.PROCESSED_REMOVE_DATA))
        







if __name__ == '__main__':
    unittest.main()
