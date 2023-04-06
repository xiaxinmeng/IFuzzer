proc = subprocess.Popen(['whoami'], stdout=subprocess.PIPE,
stderr=subprocess.STDOUT)
stdout, stderr = proc.communicate()