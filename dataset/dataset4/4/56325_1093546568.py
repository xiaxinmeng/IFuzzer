with open("setup.py", "rb") as f:
    # read smaller than the file size to fill the readahead buffer
    f.read(1)
    # seek doesn't seek
    f.seek(0)
    print("f pos=", f.tell())
    print("f.raw pos=", f.raw.tell())