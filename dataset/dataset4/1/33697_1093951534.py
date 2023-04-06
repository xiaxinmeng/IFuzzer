file = open('c:/windows/desktop/mp3/Aphex Twin - Bucephalus Bouncing Ball.mp3', 'rb')

t1 = threading.Thread(target=filesender.prepare_msgs, args=(file,'a@b.c'))

from cStringIO import StringIO
data = StringIO()
import mimetools

t2=threading.Thread(target=mimetools.encode, args=(file,data,'base64'))

import sys
if '-t1' in sys.argv:
    t1.start()
elif '-t2' in sys.argv:
    t2.start()
else:
    filesender.prepare_msgs(file, 'a@b.c')
##