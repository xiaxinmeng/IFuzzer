import mailcap
d=mailcap.getcaps()
commandline,MIMEtype=mailcap.findmatch(d, "text/*", filename="'$(xterm);#.txt")
## commandline = "less ''$(xterm);#.txt'"
import os
os.system(commandline)
## xterm starts