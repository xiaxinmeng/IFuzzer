import tracemalloc; tracemalloc.start()
import subprocess, threading, time, gc

def spawn(event) :
    subprocess.check_output("true")
    gc.collect(), gc.collect(), gc.collect()
    event.set()

def func(loops):
    event = threading.Event()
    for x in range(loops):
        event.clear()
        timer = threading.Timer(0, spawn, (event,))
        timer.start()
        event.wait()

func(100)