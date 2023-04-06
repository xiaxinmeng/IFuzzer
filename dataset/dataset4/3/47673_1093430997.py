from os import listdir
from warnings import simplefilter
simplefilter('always', DeprecationWarning)
s = "a = 2\nlistdir(b'.')\n"
exec(s)