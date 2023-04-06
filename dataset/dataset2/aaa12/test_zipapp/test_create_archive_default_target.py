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

def test_create_archive_default_target():
    source = ZipAppTest.tmpdir / 'source'
    source.mkdir()
    (source / '__main__.py').touch()
    zipapp.create_archive(str(source))
    expected_target = ZipAppTest.tmpdir / 'source.pyz'
    ZipAppTest.assertTrue(expected_target.is_file())

ZipAppTest = test_zipapp.ZipAppTest()
ZipAppTest.setUp()
test_create_archive_default_target()
