_ARCHIVE_FORMATS = {
     'gztar': (_make_tarball, [('compress', 'gzip')], "gzip'ed tar-file"),
     'bztar': (_make_tarball, [('compress', 'bzip2')], "bzip2'ed tar-file"),                      
     'ztar':  (_make_tarball, [('compress', 'compress')],
                 "compressed tar file"),
     'tar':   (_make_tarball, [('compress', None)], "uncompressed tar file"),
     'zip':   (_make_zipfile, [],"ZIP file")
     }