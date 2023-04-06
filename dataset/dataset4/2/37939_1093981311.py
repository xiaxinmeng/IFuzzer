import gzip
fin = open("/dev/urandom", "rb")
fout = gzip.GzipFile("out", "wb")
for i in range(4500): fout.write(fin.read(1024*1024))
fout.close()