proc = subprocess.Popen([r"c:\Windows\system\ping.exe","localhost"],
shell=1, stdout=subprocess.PIPE, stderr=subprocess.PIPE)