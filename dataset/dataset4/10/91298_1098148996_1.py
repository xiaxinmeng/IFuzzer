try:
    return pkg_files.joinpath(f'templates/{user_supplied_name}').read_text()
except (NoSuchFileError, IsADirectoryError):
    raise ...