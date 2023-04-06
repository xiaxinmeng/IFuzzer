while have_tasks_to_process():
   submit_tasks_to_queue()
   try:
       task_queue.join(timeout)
   except Pending:
       pass