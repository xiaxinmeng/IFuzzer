
import io
import zipfile
buf = io.BytesIO()
zf = zipfile.ZipFile(buf, mode='w')
zp = zipfile.Path(zf)
with zp.joinpath('zile-a').open('w') as fp:
    fp.write(b'contents of file-a')
zf.close()
zp.root.close()
