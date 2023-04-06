from multiprocessing import Process, set_start_method
import time
import os
import atexit


def cleanup():
    print(f"cleanup {os.getpid()}")


atexit.register(cleanup)


def run():
    time.sleep(0.1)
    print(f"process done {os.getpid()}")
    # atexit._run_exitfuncs()


if __name__ == "__main__":
    set_start_method("fork")
    process = Process(target=run)
    process.start()
    process.join()
    print("app finished")