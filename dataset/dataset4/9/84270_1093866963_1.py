_thread.start_new_thread(fork_in_thread, ())
# block the main thread: fork_in_thread() exit the process
time.sleep(60)