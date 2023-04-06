

import zipfile

zfile = zipfile.ZipFile("tmp.zip",'w')
zif = zipfile.ZipInfo("tmp/")
zfile.writestr(zif,"")
zfile.close()
