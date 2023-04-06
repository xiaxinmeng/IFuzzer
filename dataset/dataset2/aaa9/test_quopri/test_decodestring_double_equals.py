import unittest
import sys, io, subprocess
import quopri
import test_quopri

@test_quopri.withpythonimplementation
def test_decodestring_double_equals():
    (decoded_value, encoded_value) = (b'123=four', b'123==four')
    QuopriTestCase.assertEqual(quopri.decodestring(encoded_value), decoded_value)

QuopriTestCase = test_quopri.QuopriTestCase()
test_decodestring_double_equals()
