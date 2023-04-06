import hotshot.log

WHAT_ADD_INFO = 0x13
open("./tmp", "w").write(chr(WHAT_ADD_INFO))
logreader = hotshot.log.LogReader("./tmp")