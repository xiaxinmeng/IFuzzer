with shutil.atomic_write("foo", "wb") as f:
    f.write("mycontents")