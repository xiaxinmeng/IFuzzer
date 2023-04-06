def do_loop():
    while True:
        pass

t = threading.Thread(target=do_loop)
t.setDaemon(True)
t.start()

f = os.open(sys.argv[1], os.O_RDONLY)

for i in range(4, 1000):
    os.dup2(f, i)