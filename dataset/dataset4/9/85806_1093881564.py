import zipfile
srcfile=zipfile.ZipFile('file.zip')
a=zipfile.Path(srcfile,"data1.bin").read_bytes()
b=zipfile.Path(srcfile,"data2.bin").read_bytes()