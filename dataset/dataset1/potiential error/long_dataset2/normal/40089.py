import os, _thread, threading, time

def fork_in_thread():
    pid = os.fork()
    if pid:
        # parent
        os._exit(0)

    # child process
    print(f"child process: {threading.current_thread()=}")
    print(f"child process: {threading._main_thread=}")

print(f"parent process: {threading.current_thread()=}")
print(f"parent process: {threading._main_thread=}")

_thread.start_new_thread(fork_in_thread, ())
# block the main thread: fork_in_thread() exit the process
time.sleep(60)
