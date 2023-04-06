if hasattr(os, "symlink"):
    if not os.path.exists(dest):
        os.symlink(src, dest)