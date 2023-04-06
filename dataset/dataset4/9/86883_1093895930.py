import sys, threading

def run():
    for i in range(100):
        sys.stderr.write(' =.= ' * 10000)

if __name__ == '__main__':
    threading.Thread(target=run, daemon=True).start()