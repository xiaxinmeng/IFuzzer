import zipimport

class BadStr(str):
    def replace(self, old, new):
        return 42