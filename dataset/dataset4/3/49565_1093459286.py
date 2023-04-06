signal.signal(MY_SIGNAL, signal_handler)
threading.Thread(target = my_main_function)
thread.start()
thread.join()