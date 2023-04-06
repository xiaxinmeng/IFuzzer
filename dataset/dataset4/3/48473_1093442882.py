import zipfile

z = zipfile.ZipFile('aaa.zip', mode='w')
z.writestr('aa.py', 'def x(): print "hi there"\n\ndef y(): print "hi"')
z.close()