import pkg_resources

import urllib
import multiprocessing

def sub():
    print("about to call getproxies !")
    urllib.getproxies()
    print("getproxies has completed !")
    
process = multiprocessing.Process(target=sub)
process.start()

print("hi!")

process.join()
