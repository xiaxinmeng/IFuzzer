def start_thread():
    t = Thread(target=lambda: f(t))
    t.obj = [0]
    t.start()

for _ in range(n_threads):
    start_thread()