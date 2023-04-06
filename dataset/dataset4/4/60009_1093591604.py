print('This goes to stdout')
with redirect_stdout(sys.stderr):
     print('This goes to stderr')
     print('So does this')
print('This goes to stdout')
with redirect_stdout() as s:
     print('This goes to the io.StringIO instance "s"')
     print('So does this')
print('This goes to stdout')