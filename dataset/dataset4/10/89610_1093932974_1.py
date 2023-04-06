class ExtensionTest(TestCase):
    def test_stub(self):
        self.assertIn('.pyi', common.python_extensions)
        self.assertIn('.pyi', common.extension_string)