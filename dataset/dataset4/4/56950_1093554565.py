def move2(src, dst):
    try:
        os.link(src, dst)
    except OSError as err:
        # handle error appropriately, raise shutil.Error if dst exists,
        # or use shutil.copy2 if dst is on a different filesystem.
        pass
    else:
        os.unlink(src)