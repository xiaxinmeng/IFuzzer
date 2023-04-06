import code
import io
import os
import sys

def run():
    print(sys.stdin.buffer.raw)
    dupstdin = os.dup(0)
    try:
        code.InteractiveConsole().interact()
    except SystemExit:
        pass
    finally:
        # Workaround: Without this line, the second call to run() will fail with a ValueError when
        # it tries to call input().
        sys.stdin = io.TextIOWrapper(
            io.BufferedReader(io.FileIO(dupstdin, mode='rb', closefd=False)),
            encoding='utf8')

run()
run()