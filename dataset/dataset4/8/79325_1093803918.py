import tempfile
import pathlib

def test():
  with tempfile.TemporaryDirectory(prefix='test-bad-') as tmpdir:
    tmpdir = pathlib.Path(tmpdir)
    subdir = tmpdir / 'sub'
    subdir.mkdir()
    with open(subdir / 'file', 'w'):
      pass
    subdir.chmod(0o600)

if __name__ == '__main__':
  test()