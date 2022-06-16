import pathlib, json
import unittest
import os, sys
# added to fix relative path import problem.
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


# from unittest import mock
# from unittest.mock import patch

from lib.fetch_github_repo import create_file_name, filter_data, process_links
from lib.github_cred import credentials
from lib.snapshot import get_database

DUMMY_DIR = pathlib.Path.cwd().joinpath('unit_test')
DUMMY_RAW_GITHUB_DATA = DUMMY_DIR.joinpath('dummy_raw_github_data.json')
DUMMY_OLD_DB = DUMMY_DIR.joinpath('dummy_data1.json')
DUMMY_NEW_DATA = DUMMY_DIR.joinpath('dummy_data2.json')

DUMMY_OLD_TEST_DB =[{"name":"BryonS-project0","default_branch":"master","updated_at":1654978288.0,"pushed_at":1655089511.0},{"name": "Advent_of_Code","default_branch": "main","updated_at": 1638662138.0,"pushed_at": 1638662135.0},{"name": "algorithms","default_branch": "main","updated_at": 1652769527.0,"pushed_at": 1652769524.0},{"name": "audioBook-Scraper","default_branch": "main","updated_at": 1648329351.0,"pushed_at": 1629075600.0},{"name": "audiobook_scraper","default_branch": "main","updated_at": 1652389860.0,"pushed_at": 1653092508.0}]

class Test_Snapshot(unittest.TestCase):
    def test_read_file(self):
        self.assertEqual(get_database(DUMMY_DIR, DUMMY_OLD_DB), DUMMY_OLD_TEST_DB)



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
        with open(DUMMY_RAW_GITHUB_DATA) as f3:
            cls.RAW_GITHUB_DATA = json.load(f3)

    def test_create_file_name(self):
        self.assertEqual(create_file_name(self.USER, 1234567890), f"{self.USER}_1234567890.zip")
        self.assertEqual(create_file_name(f" {self.USER} ", " 1234567890 "), f"{self.USER}_1234567890.zip")
        self.assertEqual(create_file_name(f"{self.USER} ", 1234567890.009), f"{self.USER}_1234567890.009.zip")

    def test_filter_data(self):
        TEST_GITHUB_DATA = [{'name': 'BryonS-project0', 'default_branch': 'master', 'updated_at': 1654978288.0, 'pushed_at': 1655014376.0, 'owner': '2206-devops-batch'}, {'name': 'Advent_of_Code', 'default_branch': 'main', 'updated_at': 1638662138.0, 'pushed_at': 1638662135.0, 'owner': 'webmastersmith'}]
        self.assertEqual(filter_data(self.RAW_GITHUB_DATA), TEST_GITHUB_DATA)

    def test_process_links(self):
        DUMMY_DATA_FILE_PATH = DUMMY_DIR.joinpath('temp_dummy_data.json')
        DUMMY_DOWNLOAD = [{'name': 'BryonS-project0', 'default_branch': 'master', 'updated_at': 1654978287.0, 'pushed_at': 1655089511.0}, {'name': 'Advent_of_Cod', 'default_branch': 'main', 'updated_at': 1638662138.0, 'pushed_at': 1638662135.0}, {'name': 'audioBook-Scrape', 'default_branch': 'main', 'updated_at': 1648329351.0, 'pushed_at': 1629075600.0}, {'name': 'audiobook_scrape', 'default_branch': 'main', 'updated_at': 1652389860.0, 'pushed_at': 1653092508.0}]

        DUMMY_REMOVE_LIST = [{'name': 'BryonS-project0', 'default_branch': 'master', 'updated_at': 1654978288.0, 'pushed_at': 1655089511.0}]

        self.assertEqual(process_links(self.OLD_DB, self.NEW_DATA, DUMMY_DATA_FILE_PATH), (DUMMY_DOWNLOAD, DUMMY_REMOVE_LIST))
        







if __name__ == '__main__':
    unittest.main()
