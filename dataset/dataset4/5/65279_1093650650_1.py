proc = yield from create_subprocess_exec("ls", stdout=subprocess.PIPE)
stdout, _ = yield from proc.communicate()