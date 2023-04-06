if sys.platform[:3] == 'win' or sys.platform == 'darwin':
   requires('largefile', 'test requires %s bytes and a long time to run' % str(0x180000000))