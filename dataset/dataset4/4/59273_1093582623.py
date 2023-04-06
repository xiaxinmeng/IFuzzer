import sys
while True:
    chunk = sys.stdin.read(1000)
    if not chunk:
        break
    # process