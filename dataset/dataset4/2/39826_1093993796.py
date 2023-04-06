import zipfile
z = zipfile.ZipFile( "file.zip", "w" )
z.write( "file.txt", u"file.txt" )
z.close()