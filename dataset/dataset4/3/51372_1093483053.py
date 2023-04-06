while True:
    fail=failureObject()
    tlist = []
    for x in ["data1", "data2"]:
        t = threading.Thread(target=checkAlive, args = (fail, x), name=x)
        t.start()
        tlist.append(t)

    for x in tlist:
        t.join()