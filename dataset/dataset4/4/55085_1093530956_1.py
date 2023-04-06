import zipfile

zfile=raw_input("Please input zip's file name\n")
zipf = zipfile.ZipFile( zfile, 'r' )
zipf.setpassword('844')
zipf.extractall()
zipf.close()  