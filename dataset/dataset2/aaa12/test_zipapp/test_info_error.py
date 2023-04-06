import io
import pathlib
import stat
import sys
import tempfile
import unittest
import zipapp
import zipfile
from test.support import requires_zlib
from unittest.mock import patch
import test_zipapp

def test_info_error():
    target = ZipAppCmdlineTest.tmpdir / 'dummy.pyz'
    args = [str(target), '--info']
    with ZipAppCmdlineTest.assertRaises(SystemExit) as cm:
        zipapp.main(args)
    ZipAppCmdlineTest.assertTrue(cm.exception.code)

ZipAppCmdlineTest = test_zipapp.ZipAppCmdlineTest()
ZipAppCmdlineTest.setUp()
test_info_error()
