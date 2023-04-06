import tarfile


def list_tar(archive):
    if tarfile.is_tarfile(archive):
        kwargs = {'fileobj' if hasattr(archive, 'read') else 'name': archive}
        t = tarfile.open(**kwargs)
        return [member.name for member in t.getmembers()]
    return []


if __name__ == '__main__':
    path = 'archive.tar.gz'
    print(list_tar(path))
    print(list_tar(open(path, 'rb')))