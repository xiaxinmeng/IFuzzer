def _shutdown():
   # add these checking first
   if( _main_thread.isDaemon() is False or _main_thread.is_alive() is False ):
       return