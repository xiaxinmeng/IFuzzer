def start():
    a = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    a.bind(("", 8080))
    a.set_inheritable(True)

    thread = threading.Thread(target=abc, args=(a.fileno(),))
    thread.start()

    time.sleep(2)
    print("Main thread exiting, socket is still valid: " + str(a) + "\n")

def abc(b):
    sock = socket.socket(fileno=b)
    for _ in range(3):
        print("Passed as an argument:" + str(sock) + "\n=====================")

        time.sleep(1.1)

start()