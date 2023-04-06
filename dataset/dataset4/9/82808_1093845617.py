def copy(self, target):
    if not self.is_file():
        # No support for directories here
        raise ValueError("Path must point to a regular file")
    # copy() appends filename when Path is copied to a directory
    # see shutil.copy() docstring and source for details
    target = shutil.copy(self, target)
    return self.__class__(target)