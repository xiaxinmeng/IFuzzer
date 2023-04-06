
import asyncio
import subprocess
import time


def try_error():
    for i in range(1,500):
        print(i)
        try:
            subprocess.run(["ls", "-l"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        except subprocess.CalledProcessError as e:
            print(f"Exception raised {e.stderr}\nOutput {e.stdout}")



def definite_error():
    w = asyncio.get_child_watcher()
    l = asyncio.get_event_loop()
    try_error()


if __name__ == "__main__":
    definite_error()
