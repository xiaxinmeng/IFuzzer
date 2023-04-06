
import gzip

blob = b"The quick brown fox jumps over the lazy dog." * 32

with gzip.GzipFile("fast.gz", mode="wb", compresslevel=1) as outfile:
    outfile.write(blob)

with gzip.GzipFile("best.gz", mode="wb", compresslevel=9) as outfile:
    outfile.write(blob)
