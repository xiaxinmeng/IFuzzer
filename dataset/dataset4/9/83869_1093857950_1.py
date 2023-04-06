import tarfile
t = tarfile.open('sample.tar')
print('members', t.getmembers())
print('offset', t.offset)