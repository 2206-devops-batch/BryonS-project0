from urllib.request import Request, urlopen
import base64, json, re
import pathlib


def get(user, token):
    URL_USER = 'https://api.github.com/user'
    URL_REPO = f'https://api.github.com/users/{user}/repos?per_page=100'

    base64string = base64.b64encode(bytes('%s:%s' % (user, token),'ascii'))

    req =Request(URL_REPO)
    req.add_header("Authorization", "Basic %s" % base64string.decode('utf-8'))
    req.add_header("Accept", 'application/vnd.github.v3+json')
    res = urlopen(req)

    status = res.status
    print(status)

    # pull all the pages
    headers = res.getheaders()
    pathlib.Path.cwd().joinpath('avoid', 'headers.json').write_text(json.dumps(headers, indent=4))

    return json.loads(res.read())


def processLinks(linkList):
    pass
    #[
    #  "Link", 
    # "<https://api.github.com/user/17347091/repos?page=2>; rel=\"next\", 
    # <https://api.github.com/user/17347091/repos?page=2>; rel=\"last\""
    #],

    # re