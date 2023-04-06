tarfile.open('tarfile-bug.tar', 'w')
tar.add('tarfile-bug-f1')
tar.add('tarfile-bug-f2')
tar.close()