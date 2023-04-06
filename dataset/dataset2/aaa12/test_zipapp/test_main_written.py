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

def test_main_written():
    source = ZipAppTest.tmpdir / 'source'
    source.mkdir()
    (source / 'foo.py').touch()
    target = ZipAppTest.tmpdir / 'source.pyz'
    zipapp.create_archive(str(source), str(target), main='pkg.mod:fn')
    with zipfile.ZipFile(str(target), 'r') as z:
        ZipAppTest.assertIn('__main__.py', z.namelist())
        ZipAppTest.assertIn(b'pkg.mod.fn()', z.read('__main__.py'))

ZipAppTest = test_zipapp.ZipAppTest()
ZipAppTest.setUp()
test_main_written()
