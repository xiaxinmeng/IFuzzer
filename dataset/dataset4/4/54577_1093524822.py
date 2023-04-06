pytb
"""
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
  File "/usr/local/lib/python2.7/distutils/command/upload.py", line 194, in upload_file
    self.announce('-'*75, result, '-'*75)
TypeError: announce() takes at most 3 arguments (4 given)
"""
