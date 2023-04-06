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

def test_read_missing_shebang():
    source = ZipAppTest.tmpdir / 'source'
    source.mkdir()
    (source / '__main__.py').touch()
    target = ZipAppTest.tmpdir / 'source.pyz'
    zipapp.create_archive(str(source), str(target))
    ZipAppTest.assertEqual(zipapp.get_interpreter(str(target)), None)

ZipAppTest = test_zipapp.ZipAppTest()
ZipAppTest.setUp()
test_read_missing_shebang()
