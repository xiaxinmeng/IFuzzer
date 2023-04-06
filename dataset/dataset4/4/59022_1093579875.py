class ExtendPathBaseTests(unittest.TestCase):
    def test_input_string(self):
        path = 'path'
        name = 'foo'
        self.assertEqual('path', pkgutil.extend_path(path, name))

    def test_parent_package_raise_key_error(self):
        path = ['path']
        # sys.modules['foo'] raise KeyError
        name = 'foo.bar'
        self.assertEqual(['path'], pkgutil.extend_path(path, name))

    def test_parent_package_raise_attr_error(self):
        path = ['path']
        # datetime module don't have __path__ attr
        name = 'datetime.date'
        self.assertEqual(['path'], pkgutil.extend_path(path, name))