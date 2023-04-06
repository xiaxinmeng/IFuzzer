from __future__ import print_function

from os import openpty
read, write = openpty()

from subprocess import Popen
proc = Popen(
    ('echo', 'ok'),
    stdout=write,
    close_fds=True,
)

from os import fdopen
fdopen(write, 'w').close()
with fdopen(read) as stdout:
    print('STDOUT', stdout.read())

print('exit code:', proc.wait())