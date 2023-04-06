replacements = {'/1':'/01', '9/':'09/', '7/':'07/'}
file2 = open(r"c:\users\liddvdp\desktop\IBC CAP OUT.txt", "w")
with open(r"c:\users\liddvdp\desktop\IBC CAP.txt", "r") as reader:
         for line in reader:
             for src, target in replacements.items():
                 line = line.replace(src, target)
                 file2.write(line)