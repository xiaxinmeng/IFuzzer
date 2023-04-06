def remove_readonly(func, path, excinfo):
    os.chmod(path, stat.S_IWRITE)
    func(path)