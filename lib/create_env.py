import pathlib, time
from lib.github_cred import getUserToken


# root directory
DIR = pathlib.Path.cwd()

def isFileExist(dir, filename):
    return dir.joinpath(filename).exists()


def env(USER='', TOKEN=''):
    if not isFileExist(DIR, '.env'):
        makeEnv = input('GitHub needs you to be "authorized" to get your private repos.\nI can store your Github credentials in a secret ".env" file, so you don\'t have to add them every time.\n Would you like me to create one for you? (y|n) ')
        print('\n')
        if makeEnv == 'y' or makeEnv == 'yes':
            USER = ''
            TOKEN = ''
            USER, TOKEN = getUserToken(USER, TOKEN)
            n='\n'
            DIR.joinpath('.env').write_text("USER={}{}TOKEN={}".format(USER, n,TOKEN))
            print('\n')
            # check if .gitignore exist
            if not isFileExist(DIR, '.gitignore'):
                # create it
                DIR.joinpath('.gitignore').write_text("__pycache__\nsnapshot\nvenv\n.env")
                print('Ok great! I created a ".gitignore" file for you and added .env to it.\nYour secrets are safe with me. :-)')
                print('\n')
            else:
                #read .gitignore and append it if .env is not listed.
                with open(DIR.joinpath('.gitignore'), 'r+') as f:
                    isEnv = [x for x in f.readlines() if x == '.env\n']
                    # .env does not exist in the .gitignore, append it.
                    if not isEnv:
                        #append to bottom of .gitignore
                        f.write('\n.env')
                        print('Ok great! I added ".env" to your .gitignore file.\nYour secrets are safe with me. :-)')
                        print('\n')
                    else:
                        print('I checked your .gitignore file and you have ".env" in there. Great job!')
                        print('\n')
                
    return (USER, TOKEN)
