import zipfile
zipFileObject = zipfile.ZipFile(archiveName,'a')
zipFileObject.remove(fileToRemove)
zipFileObject.close()