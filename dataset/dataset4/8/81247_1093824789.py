cmd = ('bash', '--init-file', 'foo')
os.execvp(cmd[0], cmd)  # never returns