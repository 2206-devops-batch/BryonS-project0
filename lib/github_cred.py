from dotenv import load_dotenv
load_dotenv()
import getpass, os


def getUserToken(USER='', TOKEN=''):
    # logic
    if not USER:
        USER = input("What is your Github user name? ")
        print('\n')

    if not TOKEN:
        print('Your GitHub TOKEN can be found or created on GitHub.\nGo to Settings / Developer Settings / Personal access tokens\n')
        TOKEN = getpass.getpass('Please copy and paste your Github Token: ')
    return (USER.strip(), TOKEN.strip())


# Get Github Login credentials
def credentials(USER='', TOKEN=''):
    # if unittest does not pass in test data, get real data.
    if not USER and not TOKEN:
        USER = os.getenv('USER')
        TOKEN = os.getenv('TOKEN')

    # logic
    if not USER or not TOKEN:
        USER, TOKEN = getUserToken(USER, TOKEN)

    return (USER.strip(), TOKEN.strip())

