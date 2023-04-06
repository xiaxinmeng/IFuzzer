if os.path.ismount(path):
    try:
        unmount_func(path)
        _shutil.rmtree(path)
    except FileNotFoundError:
        pass