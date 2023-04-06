code = r"import sys; sys.stdout.buffer.write('a\r\nb'.encode('utf-16'))"
args = [sys.executable, '-c', code]
popen = Popen(args, universal_newlines=True, stdin=PIPE, stdout=PIPE)
print(popen.communicate(input=''))