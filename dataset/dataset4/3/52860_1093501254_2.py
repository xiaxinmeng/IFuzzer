import gzip
import io

f = gzip.GzipFile('hamster', 'wb')
f.write("some data")
f.close()

f = gzip.GzipFile('hamster', 'rb')
r = io.BufferedReader(f)
lines = [line for line in r]
r.close()