pytb
"""
Submitting dist/bsddb3-5.1.1.tar.gz to http://pypi.python.org/pypi
Upload failed (400): A file named "bsddb3-5.1.1.tar.gz" already exists for  bsddb3-5.1.1. To fix problems with that file you should create a new release.
Traceback (most recent call last):
  File "setup.py", line 5, in <module>
    import setup2
  File "/home/pybsddb/setup2.py", line 415, in <module>
    'Programming Language :: Python :: 3.2',
  File "/usr/local/lib/python2.7/distutils/core.py", line 152, in setup
    dist.run_commands()
  File "/usr/local/lib/python2.7/distutils/dist.py", line 953, in run_commands
    self.run_command(cmd)
  File "/usr/local/lib/python2.7/distutils/dist.py", line 972, in run_command
    cmd_obj.run()
  File "/usr/local/lib/python2.7/distutils/command/upload.py", line 60, in run
    self.upload_file(command, pyversion, filename)
  File "/usr/local/lib/python2.7/distutils/command/upload.py", line 189, in upload_file
    self.announce('-'*75, result.read(), '-'*75)
UnboundLocalError: local variable 'result' referenced before assignment
"""
