class OriginalZipImport(zipimport.zipimporter):
    """
    Original zipimporter class. Modified for requirements of this import hook.
    """
    # Sadly I have to manually specify the file extensions the original
    # zipimporter supports to bypass an AttributeError.
    # according to https://docs.python.org/3.6/library/zipimport.html
    # zipimport only allows importing ``.py`` and ``.pyc`` files from zips.
    extensions = ['.py', '.pyc']

    def __init__(self, archivepath):
        super(OriginalZipImport, self.inst).__init__(self, archivepath)

    def find_loader(self, fullname, path=None):
        """
        Original find_loader.
        """
        self.inst.find_loader(fullname, path=path)

    def find_module(self, fullname, path=None):
        """
        Original find_module.
        """
        self.inst.find_module(self, fullname, path=path)

    def load_module(self, fullname):
        """
        Original load_module.
        """
        self.inst.load_module(self, fullname)