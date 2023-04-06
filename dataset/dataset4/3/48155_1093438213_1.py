p = subprocess.Popen(["python", "-c", "print 32"],
stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
p.stdin.close()
p.communicate()
('32\r\n', '')