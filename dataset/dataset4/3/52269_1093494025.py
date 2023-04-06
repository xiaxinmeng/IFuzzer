def handler( *args ):
   sys.exit(-1) #<-- terminate program


signal.signal( signal.SIGALRM, handler ) 
# set alarm to go off in one second that calls handler()
signal.alarm( 1 )


time.sleep( 3 )