def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(enum))
    tests.addTests(doctest.DocFileSuite(
            '../../Doc/library/enum.rst',
            optionflags=doctest.ELLIPSIS|doctest.NORMALIZE_WHITESPACE,
            ))
    return tests