import threading
event = threading.Event()
while True:
    if event.wait(10000):
        break