import regex as re
rx = re.compile(r'\bt(est){i<2}', flags=re.V1)
print("Prints here")
rx.findall("Some text") # Python crashes
print("Fails to print")
