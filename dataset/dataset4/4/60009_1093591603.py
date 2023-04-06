print('This goes to stdout')
with RedirectStdout(sys.stderr):
     print('This goes to stderr')
     print('So does this')
print('This goes to stdout')