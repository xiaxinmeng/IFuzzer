for i in range(1000):
    t = Crash()
    t.start()

    while t.isAlive():
         pass