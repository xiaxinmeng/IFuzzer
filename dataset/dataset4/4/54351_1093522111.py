pycon
"""
>>> import os
>>> f=open("XX","w+b")
>>> f.seek(1024*1024)
1048576
>>> f.write(b"hello")
5
>>> f.seek(1024*1024*2)
2097152
>>> f.write(b"bye")
3
>>> f.seek(0,os.SEEK_HOLE)
0
>>> f.seek(0,os.SEEK_DATA)
1048576
>>> f.seek(1048576,os.SEEK_HOLE)
1179648
>>> f.seek(1179648,os.SEEK_DATA)
2097152
>>> f.seek(2097152,os.SEEK_HOLE)
2097155
>>> fd=f.fileno()
>>> os.lseek(fd,0,os.SEEK_HOLE)
0
>>> os.lseek(fd,0,os.SEEK_DATA)
1048576
>>> os.lseek(fd,1048576,os.SEEK_HOLE)
1179648
>>> os.lseek(fd,1179648,os.SEEK_DATA)
2097152
"""
