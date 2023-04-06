def get_status(file):
    fp = open(file)
    try:
        return fp.readline()
    finally:
        fp.close()