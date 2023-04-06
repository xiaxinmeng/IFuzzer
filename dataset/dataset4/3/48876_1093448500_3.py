from code import InteractiveInterpreter

ii = InteractiveInterpreter()
source = b'print(999)'
source = str(source, 'cp1252') #<<<<<<<<<<
ii.runsource(source)