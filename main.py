#!/c/Python310/python

from lib.create_env import env
from lib import github_cred as github
from lib import snapshot
from lib import fetch_github_repo

#check .env file exist
USER, TOKEN = env()

# paths
DIR = fetch_github_repo.DIR
FILE = fetch_github_repo.GITHUB_DB_FILE_PATH

# Check for directory and database file
db = snapshot.get_database(DIR, FILE)

# Github Login Credentials
USER, TOKEN = github.credentials(USER, TOKEN)

# Github Repo
fetch_github_repo.get_repositories(USER, TOKEN, db)

print('Done!')