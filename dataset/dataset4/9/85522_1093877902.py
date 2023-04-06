
import io
import zipfile
buf = io.BytesIO()
zf = zipfile.ZipFile(buf, mode='w')
zp = zipfile.Path(zf)
with zp.joinpath('zile-a').open('w') as fp:
    fp.write('contents of file-a')
zf.close()
buf.close()
zp.root.close()
