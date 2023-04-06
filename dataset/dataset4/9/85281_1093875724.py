
class PurePath:
   
     def __new__(cls, *args):
         if cls is PurePath:
             cls = PureWindowsPath if os.name == 'nt' else PurePosixPath
         super().__new__(cls, *args) # Here we remove call to from_parts

     def __init__(self, *args):
         # We should have an __init__ in the hierarchy.
         drv, root, parts = self._parse_args(args)  # this would get the proper _flavour.
         self._drv = drv
         self._root = root
         self._parts = parts

     ...

class Path(PurePath):
     def __new__(cls, *args, **kwargs):
        if cls is Path:
            cls = WindowsPath if os.name == 'nt' else PosixPath

        # REMOVE THIS LINE: self = cls._from_parts(args, init=False) #

        if not self._flavour.is_supported:
            raise NotImplementedError("cannot instantiate %r on your system"
                                      % (cls.__name__,))
        return super().__new__(cls, *args, **kwargs) # Use super

