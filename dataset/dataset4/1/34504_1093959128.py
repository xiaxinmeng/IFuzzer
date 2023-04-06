import os


def walker(arg, dirname, filenames):
    # Create A List Of Files In A Directory
    for files in filenames:
        arg.append(os.path.join(dirname, files))

DirLst = []

os.path.walk('c:\\test\\', walker, DirLst)