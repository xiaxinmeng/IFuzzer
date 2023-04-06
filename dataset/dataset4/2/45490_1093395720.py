from os import *

def Fork():
    b = fork()
    if b < 0:
        raise Exception('fork() failed')
    return b