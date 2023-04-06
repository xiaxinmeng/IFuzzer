
sts = os.system('ls ' + longlist + ' ' + filename)
if sts: msg('"ls -l" exit status: ' + repr(sts))
