import threading
import requests
import sys

def create():
    for i in range(100):
        requests.post("http://127.0.0.1:8088/", data="acs")

if __name__ == "__main__":
    for i in range(100):
        thread = threading.Thread(target=create, args=(), daemon=True)
        thread.start()
    sys.exit()