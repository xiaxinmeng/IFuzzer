import threading
import time

def sample_thread(stop_ev):
    while not stop_ev.is_set():
        t2 = time.time() 
        stop_ev.wait(0.016999959945)
        print((time.time() - t2))

def main():
    stop_ev = threading.Event()
    sample_t = threading.Thread(target=sample_thread, args=(stop_ev, ))
    sample_t.start()

    # Other stuff here, sleep is just dummy
    time.sleep(14)

    stop_ev.set()

    print('End reached.')

if __name__ == '__main__':
    main()