env = os.environ.copy()
env['MY_VARIABLE'] = 'MY_VAL'
subprocess.Popen(... , env=env)