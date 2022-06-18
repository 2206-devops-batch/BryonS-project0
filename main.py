#!/c/Python310/python

from lib.check_dependency import get_dependencies

#check if dependency packages are installed
is_dependency_met = get_dependencies()

# make sure you have dependencies before importing files
if is_dependency_met:
    from lib.create_env import env
    from lib import github_cred as github
    from lib.snapshot import get_database, DIR
    from lib import fetch_github_repo

    #check .env file exist
    USER, TOKEN = env()

    # paths
    DIR = fetch_github_repo.SNAPSHOT_DIR
    FILE = fetch_github_repo.GITHUB_DB_FILE_PATH

    # Check for directory and database file
    db = get_database(DIR, FILE)

    # Github Login Credentials
    USER, TOKEN = github.credentials(USER, TOKEN)

    # Github Repo
    fetch_github_repo.get_repositories(USER, TOKEN, db)

    print('Done!')