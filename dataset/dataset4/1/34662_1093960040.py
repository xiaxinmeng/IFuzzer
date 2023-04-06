import thread, os, sys, time
def run():
    while 1:
        if os.fork() == 0:
            time.sleep(0.001)
            sys.stderr.write('*')
            sys.stderr.flush()
            sys.exit(0)
            break
        os.wait()

thread.start_new_thread(run, ())
while 1:
    time.sleep(0.001)
    pass