from multiprocessing.connection import Client

for i in range(1000):
    successfully_sent = False
    while not successfully_sent:
        try:
            with Client(("localhost", 10000), authkey=b"test") as client:
                client.send(i)
        except (ConnectionRefusedError, ConnectionResetError):
            continue
        successfully_sent = True