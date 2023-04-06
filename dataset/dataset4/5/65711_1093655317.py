import time

class A():
    def __init__(self):
        print("Initializing A. The time is {}".format(time.time()))

    def __del__(self):
        if time is None:
            print("time is None!")
        else:
            print("Deleting A. The time is {}".format(time.time()))

a = A()
raise SystemExit()