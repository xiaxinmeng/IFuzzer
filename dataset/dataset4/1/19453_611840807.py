# [executor_reference would be passed as an argument from _adjust_process_count()]
executor = executor_reference()
if executor is not None:
    executor._idle_worker_semaphore.release()
del executor