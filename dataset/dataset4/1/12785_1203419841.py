def iterdir_recursive(path: pathlib.Path) -> typing.Generator[pathlib.Path, None, None]:
    for child in path.iterdir():
        if child.is_dir():
            yield from iterdir_recursive(child)
        else:
            yield child