import zipfile
zipname = "reallybig.zip"
z = zipfile.ZipFile( zipname )
zi = z.infolist()
for inf in zi:
      print( inf.filename, inf.header_offset, inf.extra )  