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

def test_cmdline_copy():
    original = ZipAppCmdlineTest.make_archive()
    target = ZipAppCmdlineTest.tmpdir / 'target.pyz'
    args = [str(original), '-o', str(target)]
    zipapp.main(args)
    ZipAppCmdlineTest.assertTrue(target.is_file())

ZipAppCmdlineTest = test_zipapp.ZipAppCmdlineTest()
ZipAppCmdlineTest.setUp()
test_cmdline_copy()
