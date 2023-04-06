def create_exclusive_file(filename):
  return open(filename, "w",
              opener=lambda path, mode: os.open(path, mode|os.O_CREAT|os.O_EXCL))