grep_process = Popen(["grep", "-v", "not"], stdin=PIPE, stdout=PIPE)
cut_process = Popen(["cut", "-c", "1-10"], stdin=p1.stdout, stdout=PIPE)
grep_process.stdin.write('Hello World\n')
grep_process.stdin.close()
result = cut_process.stdout.read() # blocks forever here
assert result == "Hello Worl\n"