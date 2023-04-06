import os
import threading

def display_rss():
    os.system(f"grep ^VmRSS /proc/{os.getpid()}/status")

def wait(event):
    event.wait()

class Thread(threading.Thread):
    def __init__(self):
        super().__init__()
        self.stop_event = threading.Event()
        self.started_event = threading.Event()

    def run(self):
        self.started_event.set()
        self.stop_event.wait()

    def stop(self):
        self.stop_event.set()
        self.join()

def main():
    nthread = 1000
    display_rss()
    threads = [Thread() for i in range(nthread)]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.started_event.wait()
    display_rss()
    for thread in threads:
        thread.stop()

main()