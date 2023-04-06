BIGFILE = "pcbuild.opt"  # OK, it's not really big
import threading, mimetools
from cStringIO import StringIO

file1 = open(BIGFILE, 'rb') 
data1 = StringIO() 
t1 = threading.Thread(target=mimetools.encode,
                    args=(file1, data1, 'base64')) 
t1.start()