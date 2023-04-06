for line in fileinput.input():
   if fileinput.isfirstline() and fileinput.lineno() != 1:
      processfile()
   processline(line)
processfile()