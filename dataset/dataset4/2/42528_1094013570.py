for i in xrange(3):
    thread.start_new_thread(f, (lambda i=i:i))