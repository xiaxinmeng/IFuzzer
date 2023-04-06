for i in range(100000):
    for j in range(10):
        timer = threading.Thread(target = callback)
        timer.start()
    time.sleep(1)
    print(len(threading._shutdown_locks))