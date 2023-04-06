while True:
    q.put(["data1", "data2"])
    t = Process(target=popJobs, args=(q, ))
    t.start()
    t.join()