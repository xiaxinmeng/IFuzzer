tf = tarfile.open('a.zip')
memf = tf.open('abc/def/1.txt', 'r')
zf2 = zipfile.ZipFile(memf) 