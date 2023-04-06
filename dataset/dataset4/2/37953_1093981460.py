tf = tarfile.open(self.filename, 'r')
for member in tf.getmembers():
     tf.extract(member)