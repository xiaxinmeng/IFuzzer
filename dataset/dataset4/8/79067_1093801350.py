subprocess.run('ls', input=b'', stdin=None) # this is ok

kwargs = {'input': b'', 'stdin': None}
subprocess.run('ls', **kwargs) # this throws exception