p = subprocess.Popen(..., stdout=STDOUT)
p.wait()
p.stdout.read()