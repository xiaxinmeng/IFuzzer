from os import popen2

def getoutput(cmd):
	i,o=popen2(cmd)
	result=[]
	l=o.readline()
	while l:
		result.append(l)
		l=o.readline()
	return "\n".join(result)
	o.close()
	i.close()