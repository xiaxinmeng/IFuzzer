pycon
"""
Python 2.7.2 (default, Jul 14 2011, 00:30:51) 
[GCC 4.4.3] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> import os
>>> os.getpid()
5701
>>> import socket
[...]
jcea@ubuntu:~$ cat /proc/5701/maps|grep -i ssl
7f2f467cd000-7f2f46818000 r-xp 00000000 fc:0a 131554                     /lib/libssl.so.0.9.8
7f2f46818000-7f2f46a17000 ---p 0004b000 fc:0a 131554                     /lib/libssl.so.0.9.8
7f2f46a17000-7f2f46a19000 r--p 0004a000 fc:0a 131554                     /lib/libssl.so.0.9.8
7f2f46a19000-7f2f46a1e000 rw-p 0004c000 fc:0a 131554                     /lib/libssl.so.0.9.8
7f2f46a47000-7f2f46a4f000 r-xp 00000000 fc:0a 403582                     /usr/local/lib/python2.7/lib-dynload/_ssl.so
7f2f46a4f000-7f2f46c4e000 ---p 00008000 fc:0a 403582                     /usr/local/lib/python2.7/lib-dynload/_ssl.so
7f2f46c4e000-7f2f46c4f000 r--p 00007000 fc:0a 403582                     /usr/local/lib/python2.7/lib-dynload/_ssl.so
7f2f46c4f000-7f2f46c50000 rw-p 00008000 fc:0a 403582                     /usr/local/lib/python2.7/lib-dynload/_ssl.so
"""
