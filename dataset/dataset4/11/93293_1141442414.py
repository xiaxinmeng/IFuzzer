
threads = []
for i in range(10):
  thread = threading.Thread(target=fn, args=(i,))
  thread.start()
  threads.append(thread)
