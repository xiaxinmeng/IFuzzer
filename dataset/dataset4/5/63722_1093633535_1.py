import logging
import time

def using_handler():
    filename = "test.log"
    handler = logging.FileHandler(filename, mode="w", delay=1)
    handler.close()

def test():
    while True:
        using_handler()
        time.sleep(.01)

if __name__ == "__main__":
    test()