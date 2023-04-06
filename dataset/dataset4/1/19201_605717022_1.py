
print("Executing:", command)
sts = os.system(command)
if sts:
    print("Exit status:", sts)
