for i in range(10000):
    f = subprocess.Popen('/tmp/test')
    f.wait()