import os
import shutil

def onerror(func, path, exc_info):
    print(func)

os.mkdir("test")
os.chmod("test", 0)
shutil.rmtree("test", onerror=onerror)