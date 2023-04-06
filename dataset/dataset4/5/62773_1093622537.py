import unittest

class Test(unittest.TestCase):

    def test_warning(self):
        import warnings

        with self.assertWarns(RuntimeWarning) as cm:
            raise ValueError('f')
            warnings.warn('f', RuntimeWarning)
        print(repr(cm.warning))