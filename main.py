from lib import github_cred as github
from lib import snapshot
from lib import fetch_github_repo

import pathlib, json

# # Check for directory and database file
# db = snapshot.database()
# print(db)


# Github Login Credentials
USER, TOKEN = github.credentials()
# Github Repo
data = fetch_github_repo.get(USER, TOKEN)
# save file to disk
pathlib.Path.cwd().joinpath('avoid', 'db.json').write_text(json.dumps(data, indent=4))


# Temp function to read file from disc for testing.
def readFiles():
    # read headers
    json_headers = pathlib.Path.cwd().joinpath('avoid', 'headers.json').read_text()
    headers = json.loads(json_headers)
    print(headers)
    # read db
    json_data = pathlib.Path.cwd().joinpath('avoid', 'db.json').read_text()
    data = json.loads(json_data)
    print(len(data))

readFiles()
# will be removed!!!!!!!!!


# check for updated repos
# download updated repos
# save new db file with updated repo items.

