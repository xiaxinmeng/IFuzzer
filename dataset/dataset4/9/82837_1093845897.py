mt = mimetypes.MimeTypes()
for fn in mimetypes.knownfiles:
    if os.path.isfile(fn):
        mt.read(fn)