tempdir = unicode(tempfile.gettempdir(), 'mbcs')
mkdtemp(suffix='foo', dir=tempdir)