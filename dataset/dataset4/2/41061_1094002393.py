class Unicode(varchar):
    def __init__(self, columnName=None,
appEncoding="iso-8859-1"):
        datatype.__init__(self, columnName)
        self._appEncoding = appEncoding