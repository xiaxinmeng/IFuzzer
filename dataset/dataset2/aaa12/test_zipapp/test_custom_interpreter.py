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

def test_custom_interpreter():
    source = ZipAppTest.tmpdir / 'source'
    source.mkdir()
    (source / '__main__.py').touch()
    target = ZipAppTest.tmpdir / 'source.pyz'
    zipapp.create_archive(str(source), str(target), interpreter='python')
    with target.open('rb') as f:
        ZipAppTest.assertEqual(f.read(2), b'#!')
        ZipAppTest.assertEqual(b'python\n', f.readline())

ZipAppTest = test_zipapp.ZipAppTest()
ZipAppTest.setUp()
test_custom_interpreter()
