from test import support
import unittest

class Tests(unittest.TestCase):
    def test_import_fresh(self):
        support.import_fresh_module('importlib.machinery',
            fresh=('importlib',),
            blocked=('_frozen_importlib', '_frozen_importlib_external'))