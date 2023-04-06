import tempfile
import pathlib
import shutil
import os

def rmtree_error(func, path, excinfo):
  if isinstance(excinfo[1], PermissionError):
    os.chmod(os.path.dirname(path), 0o700)
    os.unlink(path)
  print(func, path, excinfo)

def test():
  tmpdir = tempfile.mkdtemp(prefix='test-good-')
  try:
    tmpdir = pathlib.Path(tmpdir)
    subdir = tmpdir / 'sub'
    subdir.mkdir()
    with open(subdir / 'file', 'w'):
      pass
    subdir.chmod(0o600)
  finally:
    shutil.rmtree(tmpdir, onerror=rmtree_error)

if __name__ == '__main__':
  test()