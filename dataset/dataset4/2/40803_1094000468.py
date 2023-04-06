import tarfile
gz = tarfile.open('test.tar.gz', 'w|gz')
gz.add('test')
gz.close()
bz2 = tarfile.open('test.tar.bz2', 'w|bz2')
bz2.add('test')
bz2.close()