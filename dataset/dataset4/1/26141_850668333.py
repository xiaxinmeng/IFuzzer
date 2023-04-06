class TaggedPath(Path):
    def add_tag(self, tag):
        ...

@TaggedPath.register
class TaggedWindowsPath(TaggedPath, WindowsPath):
    pass

@TaggedPath.register
class TaggedPosixPath(TaggedPath, PosixPath):
    pass