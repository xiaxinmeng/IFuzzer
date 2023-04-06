subProcess.stdin.flush()

for line in subProcess.stdout:
    print(">>> " + str(line.rstrip()))
    subProcess.stdout.flush()