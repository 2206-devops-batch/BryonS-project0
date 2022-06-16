from lib import github_cred as github
from lib import snapshot
from lib import fetch_github_repo

# Check for directory and database file
DIR = fetch_github_repo.DIR
FILE = fetch_github_repo.GITHUB_DB_FILE_PATH
db = snapshot.get_database(DIR, FILE)

# Github Login Credentials
USER, TOKEN = github.credentials()

# Github Repo
fetch_github_repo.get_repositories(USER, TOKEN, db)

print('Done!')