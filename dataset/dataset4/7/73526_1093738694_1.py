threads = []
for _ in range(NUM_THREADS):
    t = SocketThread('wss://echo.websocket.org/', ssl_opt={'cert_reqs': 0})
    t.start()
    threads.append(t)

sleep(4)

for t in threads:
    t.keep_running = False
    t.ws.close()  # libssl segfaults on python3.6 when closing a wss:// connection with cert_reqs=0
    t.join()
