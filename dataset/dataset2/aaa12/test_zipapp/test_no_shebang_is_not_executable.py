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

@unittest.skipIf(sys.platform == 'win32', 'Windows does not support an executable bit')
def test_no_shebang_is_not_executable():
    source = ZipAppTest.tmpdir / 'source'
    source.mkdir()
    (source / '__main__.py').touch()
    target = ZipAppTest.tmpdir / 'source.pyz'
    zipapp.create_archive(str(source), str(target), interpreter=None)
    ZipAppTest.assertFalse(target.stat().st_mode & stat.S_IEXEC)

ZipAppTest = test_zipapp.ZipAppTest()
ZipAppTest.setUp()
test_no_shebang_is_not_executable()
