import sys
from xmlrpc.client import ServerProxy, Error

def go():
    try:
        with ServerProxy("http://localhost:7777/") as proxy:
            if proxy.notepad_me():
                return 0
    except Error as e:
        pass
    return 1
sys.exit(go())
#