from subprocess import run
from time import sleep

while True:
    result = run(["python", "multi.py"], capture_output=True)
    print(result.stdout.decode('utf-8'))
    result = run(["ps", "-ef", "--forest"], capture_output=True)
    print(result.stdout.decode('utf-8'), flush=True)
    sleep(1)