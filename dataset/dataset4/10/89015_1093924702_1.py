
def load_tests(loader, _, pattern):
    pkg_dir = os.path.dirname(__file__)
    suite = AsyncioTestSuite()
    return support.load_package_tests(pkg_dir, loader, suite, pattern)


class AsyncioTestSuite(unittest.TestSuite):
    """A custom test suite that also runs setup/teardown for the whole package.

    Normally unittest only runs setUpModule() and tearDownModule() within each
    test module part of the test suite. Copying those functions to each file
    would be tedious, let's run this once and for all.
    """
    def run(self, result, debug=False):
        try:
            setUpModule()
            super().run(result, debug=debug)
        finally:
            tearDownModule()
