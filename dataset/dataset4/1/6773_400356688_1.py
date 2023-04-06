
#
# Program showing the dangers of setting the SIG_PIPE handler to the default handler (SIG_DFL).
#
# To illustrate the problem run with:
# ./foo.py dfl
#
# The program will exit in do_network_stuff() even though there is a an "except" clause.
# The do_network_stuff() simulates a remote connection that closes before it can be written to
# which happens often enough to be a hazard in practice.
#
# 
#

import signal
import sys
import socket
import os

def sigpipe_handler(sig, frame):
    sys.stderr.write("Got sigpipe \n\n\n")
    sys.stderr.flush()

def get_server_connection():
    # simulate making a connection to a remote service that closes the connection
    # before we can write to it.  (In practice a host rebooting, or otherwise exiting while we are
    # trying to interact with it will be the true source of such behavior.)
    s1, s2 = socket.socketpair()
    s2.close()
    return s1


def do_network_stuff():
    # simulate interacting with a remote service that closes its connection
    # before we can write to it.  Example: connecting to an http service and
    # issuing a GET request, but the remote server is shutting down between
    # when our connection finishes the 3-way handshake and when we are able
    # to write our "GET /" request to it.
    # In theory this function should be resilient to this, however if SIGPIPE is set
    # to SIGDFL then this code will cause termination of the program. 
    if 'dfl' in sys.argv[1:]:
        signal.signal(signal.SIGPIPE, signal.SIG_DFL)

    for x in range(5):
        server_conn = get_server_connection()
        print("about to write to server socket...")
        try:
            server_conn.send(b"GET /")
        except BrokenPipeError as bpe:
            print("caught broken pipe on talking to server, retrying...")

def work():
    do_network_stuff()
    for x in range(10000):
        print("y")
    sys.stdout.flush()


def main():
    if 'nocatch' in sys.argv[1:]:
        work()
    else:
        try:
            work()
        except BrokenPipeError as bpe:
            signal.signal(signal.SIGPIPE, signal.SIG_DFL)
            os.kill(os.getpid(), signal.SIGPIPE)


if __name__ == '__main__':
    main()


