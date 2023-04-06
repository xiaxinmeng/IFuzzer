def readf():
	#The declaration "errors='replace'" is suppposed replace characters the reader does not recognize with a dummy character such as a question mark.
	#This fix works in the interpreter, but not from the Windows command line.
	fh_read = open(my_file, errors='replace')
	for line in fh_read:
		print(line)

#Run.
readf()