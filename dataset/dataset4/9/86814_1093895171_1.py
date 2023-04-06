
@property
def success(self):
    return bool(self.oserror is None and not self.returncode)

@property
def failure(self):
    return bool(self.oserror or self.returncode)
