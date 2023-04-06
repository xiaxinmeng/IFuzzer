from test.support.script_helper import spawn_python, kill_python
p = spawn_python('-O', '-c', '...')
kill_python(p)