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

def test_cmdline_create():
    source = ZipAppCmdlineTest.tmpdir / 'source'
    source.mkdir()
    (source / '__main__.py').touch()
    args = [str(source)]
    zipapp.main(args)
    target = source.with_suffix('.pyz')
    ZipAppCmdlineTest.assertTrue(target.is_file())

ZipAppCmdlineTest = test_zipapp.ZipAppCmdlineTest()
ZipAppCmdlineTest.setUp()
test_cmdline_create()
