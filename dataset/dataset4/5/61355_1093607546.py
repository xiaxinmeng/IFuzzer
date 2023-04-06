import shutil, tarfile, tempfile

tf = tarfile.open('failing.tar.gz', 'r:gz')
workdir = tempfile.mkdtemp()
try:
    # N.B. ensure dest path is Unicode to trigger the failure
    tf.extractall(unicode(workdir))
finally:
    shutil.rmtree(workdir)