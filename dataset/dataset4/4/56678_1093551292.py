if sys.platform in ('freebsd5', 'freebsd6'):
  # On FreeBSD6, pthread_kill() doesn't work on the main thread
  # before the creation of the first thread
  import threading
  t = threading.Thread(target=lambda: None)
  t.start()
  t.join()