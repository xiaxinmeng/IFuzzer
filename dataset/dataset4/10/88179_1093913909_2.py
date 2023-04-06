tmp1 = tempfile.TemporaryFile()
os.close(tmp1.fileno())
tmp2 = tempfile.TemporaryFile()
del tmp1
tmp2.seek(0)