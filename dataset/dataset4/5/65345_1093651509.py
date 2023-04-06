import gzip
import shutil

with open(src, 'rb') as f_in:
    with gzip.open(dst, 'wb') as f_out:
        shutil.copyfileobj(f_in, f_out)