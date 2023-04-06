
#!/usr/bin/env python

import time
import multiprocessing


def master_func(event) -> None:
    print(f"Child: {event = }")
    print(f"Child: {event.is_set() = }") # Crashes here with SIGSEGV in sem_trywait
    print("Completed")


if __name__ == "__main__":
    event = multiprocessing.Event()
    context_spawn = multiprocessing.get_context("spawn")
    proc = context_spawn.Process(target=master_func, args=(event, ))
    proc.start()
    print(f"Parent: {event = }")
    print(f"Parent: {event.is_set() = }")
    proc.join()
