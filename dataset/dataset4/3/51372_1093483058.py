curThread = threading.current_thread()
print("Started subproc: PID: %d : args: %s Thread ID: %s" %(newJob.pid,
str(args), str(curThread.ident)))