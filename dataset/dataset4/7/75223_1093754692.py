
import mimetypes

print(mimetypes.guess_type('foo.manifest'))
mimetypes.add_type('text/plain', 'manifest')
print(mimetypes.guess_type('foo.manifest'))
