import zipfile
z = zipfile.PyZipFile ('test2.zip', 'w', zipfile.ZIP_DEFLATED)
z.writepy ('test')
z.close()