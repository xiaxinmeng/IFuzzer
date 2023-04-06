import bz2

arch = bz2.BZ2File( 'wxPython-src-2.8.4.0.tar.bz2','r' )
lines = arch.readlines()