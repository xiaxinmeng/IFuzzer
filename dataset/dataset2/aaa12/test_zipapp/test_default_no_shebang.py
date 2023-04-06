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

def test_default_no_shebang():
    source = ZipAppTest.tmpdir / 'source'
    source.mkdir()
    (source / '__main__.py').touch()
    target = ZipAppTest.tmpdir / 'source.pyz'
    zipapp.create_archive(str(source), str(target))
    with target.open('rb') as f:
        ZipAppTest.assertNotEqual(f.read(2), b'#!')

ZipAppTest = test_zipapp.ZipAppTest()
ZipAppTest.setUp()
test_default_no_shebang()
