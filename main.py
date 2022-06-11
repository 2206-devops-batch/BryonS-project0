# import requests
from urllib.error import HTTPError
import urllib.request
import json

from lib import github_cred as gh
from lib import snapshot as sn

# Check for directory and database file
sn.getSnapshotData()


# # Github Login Credentials
# USER, PW = gh.get()
# # for testing
# print(USER)
# print(PW)




# # Github auth
# URL = "https://api.github.com/user/repos -q"
# try:
#     response = urllib.request.urlopen('https://google.com')
#     response_status = response.status
#     response_headers = response.getheaders()
# except HTTPError as error:
#     response_status = error.code


# # print(response_status)
# print(json.dumps(response_headers, indent=4))


# with urllib.request.urlopen('https://google.com') as f:
#     print(f)
#     print(f.read(300).decode('utf-8'))



