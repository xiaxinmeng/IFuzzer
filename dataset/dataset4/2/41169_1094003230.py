def pipepager(text, cmd):
    """Page through text by feeding it to another program."""
    try:
        import locale
    except ImportError:
        encoding = "ascii"
    else:
        encoding = locale.getpreferredencoding()
    pipe = os.popen(cmd, 'w')
    try:
        pipe.write(text.encode(encoding, 'xmlcharrefreplace') if isinstance(text, unicode) else text)
        pipe.close()
    except IOError:
        pass # Ignore broken pipes caused by quitting the pager program.
import pydoc
pydoc.pipepager = pipepager
del pydoc, pipepager