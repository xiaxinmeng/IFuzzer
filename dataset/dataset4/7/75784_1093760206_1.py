import sys
sys.stdin.close()
sys.stdin = open('/dev/null', 'r')
with open('/dev/tty', 'r') as f:
    x = input('Name? ', fin=f)
print(x)