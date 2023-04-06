for (root, dirs, nondirs) in os.walk(path, followlinks=False):
    print (nondirs)