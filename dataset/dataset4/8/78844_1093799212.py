kw = {}
if hasattr(os, 'POSIX_SPAWN_USEVFORK'):
   kw['flags'] = os.POSIX_SPAWN_USEVFORK
posix_spawn(*args, **kw)