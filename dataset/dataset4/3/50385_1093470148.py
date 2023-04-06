my_env = os.environ
my_env['PYTHONIOENCODING'] = 'utf-8'
p = subprocess.Popen(shlex.split(command), stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE, env=my_env)