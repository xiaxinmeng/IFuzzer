import sys
from subprocess import Popen, PIPE
from multiprocessing import Process

def myProcess():
    Popen(["dir"], shell = True) # ERROR :(

def main():
    Popen(["dir"], stdout = PIPE, shell = True)
    Process(target = myProcess).start()
    return 0

if __name__ == "__main__":
    sys.exit(main())