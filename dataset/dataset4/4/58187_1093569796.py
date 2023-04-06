def _findLib_ldconfig(name):
       # XXX assuming GLIBC's ldconfig (with option -p)
       expr = r'/[^\(\)\s]*lib%s\.[^\(\)\s]*' % re.escape(name)
       res = re.search(expr,
                       os.popen('/sbin/ldconfig -p 2>/dev/null').read())