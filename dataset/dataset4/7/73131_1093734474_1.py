import string
def get_boundary(str):
    """ return the valid boundary parameter as per RFC 2046 page 22. """
    if len(str) > 1:
        import re
        return re.sub('[^'+
                      string.ascii_letters +
                      string.digits +
                      r""" '()+_,-./:=?]|="""
                      ,'',str
                      ).rstrip(' ')
    return str

import unittest

class boundary_tester(unittest.TestCase):
    def test_get_boundary(self):
        boundary1 = """ abc def gh< 123 >!@ %!%' """
        ref_boundary1 = """ abc def gh 123  '""" # this is the valid Boundary
        ret_value = get_boundary(boundary1)
        self.assertEqual(ret_value,ref_boundary1)

    def test_get_boundary2(self):
        boundary1 = ''.join((' ',string.printable))
        ref_boundary1 = ' 0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ\'()+,-./:?_' # this is the valid Boundary
        ret_value = get_boundary(boundary1)
        self.assertEqual(ret_value,ref_boundary1)