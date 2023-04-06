class TestOptionalsNargs1_3(ParserTestCase):

    argument_signatures = [Sig('-x', nargs=(1, 3))]
    failures = ['a', '-x', '-x a b c d']
    successes = [
        ('', NS(x=None)),
        ('-x a', NS(x=['a'])),
        ('-x a b', NS(x=['a', 'b'])),
        ('-x a b c', NS(x=['a', 'b', 'c'])),
    ]