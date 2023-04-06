def fetch():
    url = 'http://python.org/'
    request = Request(url)
    fd = urlopen(request)
    return 'ok'

fetch()
print(tracemalloc.get_traced_memory())