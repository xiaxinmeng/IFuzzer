preexec = subprocess.Preexec()
preexec.setsid()
preexec.chdir(path)

popen = subprocess.Popen(cmd, preexec=preexec)
popen.wait()