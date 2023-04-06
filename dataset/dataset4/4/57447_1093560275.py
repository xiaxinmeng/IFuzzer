return_code = shellcmd.shell_call('ls -l {}', dirname)
listing = shellcmd.check_shell_output('ls -l {}', dirname)