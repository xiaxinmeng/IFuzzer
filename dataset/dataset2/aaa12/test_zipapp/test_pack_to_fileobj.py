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

def test_pack_to_fileobj():
    source = ZipAppTest.tmpdir / 'source'
    source.mkdir()
    (source / '__main__.py').touch()
    target = io.BytesIO()
    zipapp.create_archive(str(source), target, interpreter='python')
    ZipAppTest.assertTrue(target.getvalue().startswith(b'#!python\n'))

ZipAppTest = test_zipapp.ZipAppTest()
ZipAppTest.setUp()
test_pack_to_fileobj()
