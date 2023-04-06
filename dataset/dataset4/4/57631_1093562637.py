cmd = 'python pydaemon.py'
print("Starting daemon that runs for 10 sec")
daemon = subprocess.Popen(cmd, 
                          stdout=subprocess.PIPE,
                          stderr=subprocess.PIPE,
                          shell=True)
stdout, stderr = daemon.communicate()
print("Stdout:")
print(stdout)
print("Stderr:")
print(stderr)
##################