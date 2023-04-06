if sys.platform.startswith("win"):
    def getpreferredencoding():
        import _locale
        return _locale._getdefaultlocale()[1]
else:
    def getpreferredencoding():
        result = nl_langinfo(CODESET)
        if not result and sys.platform == 'darwin':
             result = 'UTF-8'
        return result