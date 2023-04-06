with importlib.resources.path(__package__, "dir") as dir:
    os.listdir(dir)