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

def test_main_only_written_once():
    source = ZipAppTest.tmpdir / 'source'
    source.mkdir()
    (source / 'foo.py').touch()
    (source / 'bar.py').touch()
    target = ZipAppTest.tmpdir / 'source.pyz'
    zipapp.create_archive(str(source), str(target), main='pkg.mod:fn')
    with zipfile.ZipFile(str(target), 'r') as z:
        ZipAppTest.assertEqual(1, z.namelist().count('__main__.py'))

ZipAppTest = test_zipapp.ZipAppTest()
ZipAppTest.setUp()
test_main_only_written_once()
