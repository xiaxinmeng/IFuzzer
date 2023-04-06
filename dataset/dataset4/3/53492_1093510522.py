def test_getcwd_long_pathnames(self):
    if hasattr(posix, 'getcwd'):
        dirname = 'getcwd-test-directory-0123456789abcdef-01234567890abcdef'
        curdir = os.getcwd()
        base_path = os.path.abspath(support.TESTFN) + '.getcwd'