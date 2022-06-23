import subprocess
from lib.snapshot import DIR, SNAPSHOT_DIR

def get_dependencies():
    # if the snapshot directory does not exist, assume first time install.
    if not SNAPSHOT_DIR.exists():
        print('I\'m checking your installed packages.\n')
        # list installed packages and search for dependencies
        LIST = subprocess.Popen(['pip', 'list',], stdout=subprocess.PIPE).stdout.read().decode('utf-8')
        
        if LIST.find('requests') == -1 or LIST.find('python-dotenv') == -1:
            is_install_pkg = input('I couldn\'t find the needed dependencies.\nWould you like me to install them? (y|n) ')
            if is_install_pkg == 'y' or is_install_pkg == 'yes':
                try:
                    subprocess.run(['pip', 'install', '--user', '-r', '{}/requirements.txt'.format(DIR)])
                    print('\n')
                except:
                    print("Look\'s like I don\'t have permissions.\n You can install them manually:\npip install -r 'requirements.txt'\n")
                    return False
            else:
                print("\nOK, so you want to do it the hard way! :-)\npip install -r 'requirements.txt'\n")
                return False
    return True
    




