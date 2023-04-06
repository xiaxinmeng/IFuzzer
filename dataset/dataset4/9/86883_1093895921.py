import sys, threading

def run():
    for i in range(10000000):
        sys.stderr.write(' =.= ')

if __name__ == '__main__':
    threading.Thread(target=run, daemon=True).start()