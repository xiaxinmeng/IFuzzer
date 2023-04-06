import fileinput

for l in fileinput.input(openhook=fileinput.hook_encoded('iso-8859-1')):
    raw_input()