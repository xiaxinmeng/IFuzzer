import subprocess
import threading
import random

class Forkfuzz(threading.Thread):
    def run(self):
        while random.randint(0,100) > threading.active_count():
            Forkfuzz().start()

        p = subprocess.Popen(['/bin/sleep', '1'])
        p.communicate()

if __name__ == "__main__":
    while True:
        Forkfuzz().run()
---snip