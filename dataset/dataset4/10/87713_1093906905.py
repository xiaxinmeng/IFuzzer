class ZeroedZipInfo(zipfile.ZipInfo):
    def __init__(self, zinfo):
        for k in self.__slots__:
            setattr(self, k, getattr(zinfo, k))

    def __getattribute__(self, name):
        if name == "date_time":
            return (1980,0,0,0,0,0)
        if name == "external_attr":
            return 0
        return object.__getattribute__(self, name)