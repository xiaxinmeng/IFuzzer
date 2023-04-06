
import mimetypes
mimetypes.init()
MIMETYPE_ADDITIONAL_EXTENSIONS = [("text/x-r-script", ".R"), ("text/x-r2-script", ".r"),]
for (mimetype, extension) in MIMETYPE_ADDITIONAL_EXTENSIONS:
    mimetypes.add_type(mimetype, extension, strict=True)
print("mimetypes.types_map['.R'] = %s , mimetypes.guess_type('example.R')[0] = %s" % (mimetypes.types_map['.R'],mimetypes.guess_type('example.R')[0])) 
