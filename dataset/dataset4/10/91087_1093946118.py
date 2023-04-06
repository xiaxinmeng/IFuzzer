import zipfile
with zipfile.ZipFile(r'damaged.zip') as dmg:
    dmg.testzip()