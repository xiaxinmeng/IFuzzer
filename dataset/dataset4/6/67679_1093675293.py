umask = os.umask(0) # must change umask to get umask

os.umask(umask) # restore previous umask