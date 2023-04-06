if sys.version_info[:2] == (3, 3):
    stacklevel = 10
elif sys.version_info[:2] == (3, 4):
    stacklevel = 8
else:
    stacklevel = 2
warnings.warn("{} is deprecated".format(__name__), DeprecationWarning, stacklevel=stacklevel)