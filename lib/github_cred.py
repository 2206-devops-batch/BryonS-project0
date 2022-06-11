from dotenv import load_dotenv
load_dotenv()
import getpass
import os




# Get Github Login credentials
def get(): 
    USER = os.getenv('USER')
    PW = os.getenv('PW')

    # logic
    if not USER:
        USER = input("What is your Github user name? ")

    if not PW:
        PW = getpass.getpass('What is your Github password? ')
    return (USER, PW)

