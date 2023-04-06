# create a large (>4gb) file
f = open('foo.txt', 'wb')
text = 'a' * 1024**2
for i in xrange(5 * 1024):
    f.write(text)
f.close()

# now zip the file
import zipfile
z = zipfile.ZipFile('foo.zip', mode='w', allowZip64=True)
z.write('foo.txt')
z.close()