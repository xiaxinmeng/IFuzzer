import multiprocessing as mp
from time import sleep


def wait_for_event(event):
    while not event.is_set():
        sleep(0.1)


def trigger_segment_fault():
    event = mp.get_context("fork").Event()
    p = mp.get_context("spawn").Process(target=wait_for_event, args=(event,))
    p.start()  # this will show the exitcode=-SIGSEGV
    sleep(1)
    print(p)
    event.set()
    p.terminate()


if __name__ == "__main__":
    trigger_segment_fault()