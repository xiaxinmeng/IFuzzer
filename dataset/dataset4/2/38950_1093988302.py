if sys.platform == 'mac':
    # For MacPython we know where it is
    def _pardir(p): return os.path.split(p)[0]
    BGENDIR=os.path.join(sys.prefix, "Tools", "bgen", 
"bgen")
else:
    # for unix-Python we don't know, please set it yourself.
    BGENDIR="/Users/jack/src/python/Tools/bgen/bgen"