zipFile = ZipFile(filePath, 'a')
zipFile.comment = b'My new shorter comment' # 22 character long
zipFile.close()