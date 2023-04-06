for i in range(10):
    Thread(target=print, args=(i,)).start()

for i in range(10):
    def doit(i=i):
        print(i)
    Thread(target=doit).start()