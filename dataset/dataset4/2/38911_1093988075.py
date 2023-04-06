for line in fileinput.input():
   processline(line)
   if fileinput.lastline():
      processfile()