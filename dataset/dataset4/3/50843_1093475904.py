def test():
    source = open('mangled.json', 'r')
    data = json.load(source)
    source.close()
    del data
test()
time.sleep(20)