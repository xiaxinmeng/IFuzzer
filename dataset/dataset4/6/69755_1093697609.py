import socket
import ssl
import sys


def main():
    ctx = ssl.create_default_context()
    s = socket.create_connection(('www.bing.com', 443))
    s = ctx.wrap_socket(s, server_hostname='www.bing.com')
    while True:
        s.getpeercert()

        sys.stderr.write('.')
        sys.stderr.flush()


if __name__ == '__main__':
    main()