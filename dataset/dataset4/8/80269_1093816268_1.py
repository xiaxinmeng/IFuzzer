tf = tarfile.open('a.tar')
memf = tf.extractfile('abc/def/1.zip')
zf2 = zipfile.ZipFile(memf)