lp = threading.Thread(target=logger_thread, args=(logq,), daemon=True)

workers = []
for i in range(15):
    p = Process(target=worker, args=(logq,), name=f"Worker {i+1}")
    workers.append(p)

print("starting workers")
for p in workers:
    p.start()
    # no deadlock when added:
    # time.sleep(.1)

print("starting logger thread")
lp.start()