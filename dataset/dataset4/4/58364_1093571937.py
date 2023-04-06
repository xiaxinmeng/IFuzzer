class TestFileTypeWB(TempDirMixin, ParserTestCase):
    ...
    successes = [
        ...,
        ('-x - -', NS(x=sys.stdout.buffer, spam=sys.stdout.buffer)),
    ]