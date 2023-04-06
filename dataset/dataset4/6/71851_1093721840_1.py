def task():
  threading.current_thread().name = '%s_%d' % (your_prefix, num_q.get())
  num_q.task_done()
  num_q.join()  # block so that this thread cannot take a new thread naming task until all other tasks are complete.  guaranteeing we are executed once per max_workers threads.