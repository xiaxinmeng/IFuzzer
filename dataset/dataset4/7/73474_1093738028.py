def task():
    try:
        socket.getaddrinfo('www.google.com', 443)
    except Exception as e:
        print("FAIL: %s" % e)
        raise


threads = []
for i in range(50):
    t = threading.Thread(target=task)
    threads.append(t)

for t in threads:
    t.start()

for t in threads:
    t.join()

print("DONE")