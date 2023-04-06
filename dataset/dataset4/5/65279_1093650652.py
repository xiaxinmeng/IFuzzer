ls = yield from create_subprocess_exec("ls", stdout=subprocess.PIPE)
grep = yield from create_subprocess_exec("grep", "-v", "-F", ".old",
stdin=ls.stdin, stdout=subprocess.PIPE)
stdout, _ = yield from grep.communicate()