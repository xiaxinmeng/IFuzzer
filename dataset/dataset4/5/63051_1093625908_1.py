subprocesscall_thread = threading.Thread(target=subprocesscall)
subprocesscall_thread.start()
failingsubprocesscall()
subprocesscall_thread.join()