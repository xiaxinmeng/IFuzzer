def make_testcase_classes():
    for backend in backends:
        yield type(
            '{}Test'.format(backend.name),
            (TheBaseClass, unittest.TestCase),
            {'backend': backend}
        )