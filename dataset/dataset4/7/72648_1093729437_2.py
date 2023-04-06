log('starting test')

threads = (threading.Thread(target=thread1Proc, name='t1'), threading.Thread(target=thread2Proc, name='t2'))
for t in threads:
    t.start()
for t in threads:
    t.join()

log('finished test')