p1 = subprocess.Popen(["yes"], stdout=subprocess.PIPE)
p2 = subprocess.Popen(["head"], stdin=p1.stdout, stdout=subprocess.PIPE)
#p1.stdout.close()
p1.wait()