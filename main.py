from lib import github_cred as github
from lib import snapshot
from lib import fetch_github_repo

# Check for directory and database file
db = snapshot.get_database()

# Github Login Credentials
USER, TOKEN = github.credentials()

# Github Repo
fetch_github_repo.get_repositories(USER, TOKEN, db)

print('Done!')