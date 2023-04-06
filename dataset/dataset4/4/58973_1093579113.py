pycon
"""
jcea@ubuntu:~$ echo $HOME
/home/jcea
jcea@ubuntu:~$ python
Python 2.7.3 (default, Apr 12 2012, 13:11:53) 
[GCC 4.4.3] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> import os
>>> os.path.expanduser("~/a")
'/home/jcea/a'


jcea@ubuntu:/home/jcea$ export HOME=/home/jcea/
jcea@ubuntu:/home/jcea$ echo $HOME
/home/jcea/
jcea@ubuntu:/home/jcea$ python
Python 2.7.3 (default, Apr 12 2012, 13:11:53) 
[GCC 4.4.3] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> import os
>>> os.path.expanduser("~/a")
'/home/jcea/a'
"""
