
import sys
s = ''
for i in range(1,301):
    s += f"{str(i*100).zfill(10)}{'x' * 89}\n"

sys.stdout.write(s)
