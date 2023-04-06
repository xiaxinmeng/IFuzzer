if hasattr(os, "symlink"):
    if not os.path.exists(dest):
        try:
            os.symlink(src, dest)
        except OSError:
            print("no privilege")