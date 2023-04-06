class dumb(threading.Thread):
    def __init__(self):
        super(dumb, self).__init__()
    def run(self):
        while True:
            print("hi")
            time.sleep(1)    

def test():
    for i in range(2):
        bar = dumb()
        bar.start()
def main():
    p = []
    for i in range(2):
        p.append(multiprocessing.Process(target=test))
    for i in p:
        i.start()
    for i in p:
        i.join()
if __name__ == '__main__':
    main()