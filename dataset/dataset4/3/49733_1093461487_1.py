import shelve

store = shelve.open("/tmp/shelve.db", writeback=True)

class Test(object):
    pass

def main():
    store["a"] = Test()

if __name__ == '__main__':
    main()