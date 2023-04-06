t = tempfile.TemporaryDirectory(dir=".")
os.chdir(some_other_dir)
t.cleanup()