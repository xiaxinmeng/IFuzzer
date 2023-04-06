NULLBYTECERT = os.path.join(os.path.dirname(__file__) or os.curdir, "nullbytecert.pem")
for i in xrange(100):
    p = ssl._ssl._test_decode_cert(NULLBYTECERT)