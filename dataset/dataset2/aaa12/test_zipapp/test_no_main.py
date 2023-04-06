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

def test_no_main():
    source = ZipAppTest.tmpdir / 'source'
    source.mkdir()
    (source / 'foo.py').touch()
    target = ZipAppTest.tmpdir / 'source.pyz'
    with ZipAppTest.assertRaises(zipapp.ZipAppError):
        zipapp.create_archive(str(source), str(target))

ZipAppTest = test_zipapp.ZipAppTest()
ZipAppTest.setUp()
test_no_main()
