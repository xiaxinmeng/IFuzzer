def library_dir_option(self, dir):  # OLD VERSION
     return "/LIBPATH:" + dir

def library_dir_option(self, dir): # FIXED VERSION
    if ' ' in dir and not dir.startswith('"'):
        dir = '"%s"' % dir
    return "/LIBPATH:" + dir