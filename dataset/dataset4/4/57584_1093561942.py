for dirinfo in os.walk(base_dir):
    print(dirinfo.path)
    print(dirinfo.subdirs)
    print(dirinfo.files)