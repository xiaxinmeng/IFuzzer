import sys
import os
import platform

platform.mac_ver()

if sys.version_info[0] == 2:
    import urllib
else:
    import urllib.request

if os.fork() == 0:
    print ("about to call getproxies !")
    if sys.version_info[0] == 2:
        print (urllib.getproxies())
    else:
        print (urllib.request.getproxies())
    print ("getproxies has completed !")