import os
myfd = os.open("open_and_popen.py",os.O_RDONLY)

readfo = os.popen("python print_from_fd.py "+str(myfd),"r")