from multiprocessing.connection import Listener

while True:
    with Listener(("localhost", 10000), authkey=b"test") as listener:
        with listener.accept() as connection:
            print(connection.recv())