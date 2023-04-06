def child():
    def yo():
        for j in range(5):
            print(j)
    profile.runctx('yo()', globals(), locals())


def go():
    threading.Thread(target=child).start()
    time.sleep(1)