def findfiles(folder, pattern, recursive):
    prefix = '**/' if recursive else ''
    yield from(pathlib.Path(folder).glob(f'{prefix}{pattern}'))