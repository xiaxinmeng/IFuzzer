import code
import sys

for i in range(2):
    try:
        code.InteractiveConsole().interact()
        print(f'Try {i}: closed is', sys.stdin.closed)
    except SystemExit:
        print(f'Exc {i}: closed is', sys.stdin.closed)