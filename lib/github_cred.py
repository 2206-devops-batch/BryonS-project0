from dotenv import load_dotenv
load_dotenv()
import getpass
import os




# Get Github Login credentials
def credentials(): 
    USER = os.getenv('USER')
    TOKEN = os.getenv('TOKEN')

    # logic
    if not USER:
        USER = input("What is your Github user name? ")

    if not TOKEN:
        TOKEN = getpass.getpass('Please copy and paste your Github Token: ')
    return (USER.strip(), TOKEN.strip())

