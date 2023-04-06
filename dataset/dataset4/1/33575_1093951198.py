import StringIO
import shlex

s = shlex.shlex(StringIO.StringIO("hello 'world"))