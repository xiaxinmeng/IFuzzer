import pathlib
import stat
p = pathlib.Path('some file')
p.stat().st_mode & stat.S_IXUSR