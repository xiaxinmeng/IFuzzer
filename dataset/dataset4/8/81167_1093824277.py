def extract(archive_path, destination_path):
  if not tarfile.is_tarfile(archive_path):
    print ('Not a tar file')
    return
  tar = tarfile.open(archive_path, 'r')
  for info in tar.getmembers():
    tar.extractall(destination_path, members=[tar.getmember(info.name)])

destination_path = 'output'
os.mkdir(destination_path)
extract(sys.argv[1], destination_path)