import subprocess, sys

ls = subprocess.Popen(['ls', '-l', '/etc/motd'], stdout=subprocess.PIPE,)

end_of_pipe = ls.stdout

print('Result:')

for line in end_of_pipe:
    print(line.strip())