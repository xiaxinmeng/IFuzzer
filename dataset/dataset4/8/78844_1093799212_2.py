kw = {}
if sys.platform == 'linux':
   kw['use_vfork'] = True
posix_spawn(*args, **kw)