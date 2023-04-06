import atexit, sys, signal, time, threading

terminate = False
threads = []

def test_loop():
    while True:
        if terminate:
            print('stopping thread')
            break
        else:
            print('looping')
            time.sleep(1)

@atexit.register
def shutdown():
    global terminate
    print('shutdown detected')
    terminate = True
    for thread in threads:
        thread.join()

def close_handler(signum, frame):
    print('caught signal')
    sys.exit(0)

def run():
    global threads
    thread = threading.Thread(target=test_loop)
    thread.start()
    threads.append(thread)

    while True:
        time.sleep(2)
        print('main')

signal.signal(signal.SIGINT, close_handler)

if __name__ == "__main__":
    run()