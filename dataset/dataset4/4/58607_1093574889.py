from zipfile import ZipFile

z=ZipFile('test.zip','a')
z.comment='Create a new comment'
z.close()