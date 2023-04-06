import fileinput

for line in fileinput.FileInput(openhook=fileinput.hook_compressed):
    print(line.rstrip())