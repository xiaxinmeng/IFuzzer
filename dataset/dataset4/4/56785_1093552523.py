import urllib.request, gc

print("python.org")
with urllib.request.urlopen("http://www.python.org/") as page:
    content = page.read()
    print("content: %s..." % content[:40])
gc.collect()

print("imdb.com")
with urllib.request.urlopen("http://www.imdb.com/") as page:
    content = page.read()
    print("content: %s..." % content[:40])
gc.collect()

print("exit")