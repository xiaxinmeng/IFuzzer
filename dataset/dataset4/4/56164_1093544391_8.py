class TestFileTypeW(TempDirMixin, ParserTestCase):
    """Test the FileType option/argument type for writing files"""

    def setUp(self):
        super(TestFileTypeW, self).setUp()
        self.create_readonly_file('readonly')

    argument_signatures = [
        Sig('-x', type=argparse.FileType('w')),
        Sig('spam', type=argparse.FileType('w')),
    ]
    failures = ['-x', '', 'readonly']
    successes = [
        ('foo', NS(x=None, spam=WFile('foo'))),
        ('-x foo bar', NS(x=WFile('foo'), spam=WFile('bar'))),
        ('bar -x foo', NS(x=WFile('foo'), spam=WFile('bar'))),
        ('-x - -', NS(x=sys.stdout, spam=sys.stdout)),
    ]