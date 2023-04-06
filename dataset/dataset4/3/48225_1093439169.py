from sys import executable
from os import execvpe
filename = "pouet.py"
out = open(filename, "wb")
out.write(b"""# -*- coding: GBK -*-
print("--asc\xA1\xA7i--")
raise Exception("--asc\xA1\xA7i--")""")
out.close()
execvpe(executable, [executable, filename], None)