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

def test_write_shebang_to_fileobj():
    source = ZipAppTest.tmpdir / 'source'
    source.mkdir()
    (source / '__main__.py').touch()
    target = ZipAppTest.tmpdir / 'source.pyz'
    zipapp.create_archive(str(source), str(target), interpreter='python')
    new_target = io.BytesIO()
    zipapp.create_archive(str(target), new_target, interpreter='python2.7')
    ZipAppTest.assertTrue(new_target.getvalue().startswith(b'#!python2.7\n'))

ZipAppTest = test_zipapp.ZipAppTest()
ZipAppTest.setUp()
test_write_shebang_to_fileobj()
