import subprocess

testfile = open('testfile.notexecutable', 'wb')
testfile.close()
subprocess.check_call(['testfile.notexecutable'])