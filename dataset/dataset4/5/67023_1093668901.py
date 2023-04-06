dir = tempfile.TemporaryDirectory()
self.addCleanup(dir.cleanup)  # In case removal after chdir() fails
self.addCleanup(os.chdir, os.getcwd())
os.chdir(dir.name)
try:
    dir.cleanup()
except OSError as err:  # Invalid argument on Solaris
    self.skipTest("Couldn't remove current directory: {}".format(err))