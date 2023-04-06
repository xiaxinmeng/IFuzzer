import subprocess
p = subprocess.Popen("nonex", shell=True)
print(p.wait())