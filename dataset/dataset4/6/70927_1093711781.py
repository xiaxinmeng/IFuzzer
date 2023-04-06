
with tarfile.open(name=tarball_path) as tar_fd:
    tar_fd.extractall(path=path)
