class TaggedPath(Path):
    def __new__(cls, *args, **kwargs):
        ...  # return either TaggedWindowsPath or TaggedPosixPath

    def add_tag(self, tag):
        ...

class TaggedWindowsPath(TaggedPath, WindowsPath):
    pass

class TaggedPosixPath(TaggedPath, PosixPath):
    pass