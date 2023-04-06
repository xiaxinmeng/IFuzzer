import CodeWarrior, time

cw = CodeWarrior.CodeWarrior(start=1)
time.sleep(5)
cw.activate()
cw.open(file1)
cw.disassemble_file(file2)
time.sleep(5)
xtext = app('CodeWarrior IDE').document[1].text