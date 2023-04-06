import time
def demo():
    for i in range(1, 101):
        print("\rUpdating record %d" % i, end='', flush=True)
        time.sleep(0.1)
    print()