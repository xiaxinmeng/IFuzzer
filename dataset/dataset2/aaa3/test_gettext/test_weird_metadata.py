import os
import base64
import contextlib
import gettext
import unittest
from test import support
from test.support import os_helper
import builtins
import test_gettext

def test_weird_metadata():
    info = WeirdMetadataTest.t.info()
    WeirdMetadataTest.assertEqual(len(info), 9)
    WeirdMetadataTest.assertEqual(info['last-translator'], 'John Doe <jdoe@example.com>\nJane Foobar <jfoobar@example.com>')

WeirdMetadataTest = test_gettext.WeirdMetadataTest()
WeirdMetadataTest.setUp()
test_weird_metadata()
