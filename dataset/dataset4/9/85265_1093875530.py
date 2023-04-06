import threading
import time
from functools import partial
from http.server import HTTPServer, SimpleHTTPRequestHandler


def serve_http(server):
    server.serve_forever(poll_interval=2.5)

def main():
    with HTTPServer(('', 8000), SimpleHTTPRequestHandler) as server:
        t = threading.Thread(target=partial(serve_http, server))
        t.start()

        time.sleep(3)

        start = time.time()
        print('shutdown')
        server.shutdown()
        print(f'time it took: {time.time() - start}')


if __name__ == "__main__":
    main()