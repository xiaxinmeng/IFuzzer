import os
import subprocess

cmd32 = os.path.join(os.environ['SYSTEMROOT'], 'SysWOW64', 'cmd.exe')
subprocess.call('{} /c set SYSTEMROOT'.format(cmd32), env=os.environ)