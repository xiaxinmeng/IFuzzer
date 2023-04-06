while True:
  job = queue.get()
  if job is None:
     break
  audio.play(*job)
  queue.task_done()