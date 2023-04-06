args = [sys.executable, '-c', 'pass']

popen = Popen(args, universal_newlines=False, stdin=PIPE, stdout=PIPE, stderr=PIPE)
print(popen.communicate())

popen = Popen(args, universal_newlines=True, stdin=PIPE, stdout=PIPE, stderr=PIPE)
print(popen.communicate())