from pathlib import Path, PurePath
# fails
tuple(Path('/etc').glob(PurePath('passwd')))    # TypeError
tuple(Path('/etc').rglob(PurePath('passwd')))   # TypeError
tuple(Path('C:\\').glob(PurePath('Windows')))   # AttributeError
tuple(Path('C:\\').rglob(PurePath('Windows')))  # AttributeError
# works
from os import fspath
tuple(Path('/etc').glob(fspath(PurePath('passwd'))))
tuple(Path('/etc').rglob(fspath(PurePath('passwd'))))
tuple(Path('C:\\').glob(fspath(PurePath('Windows'))))
tuple(Path('C:\\').rglob(fspath(PurePath('Windows'))))