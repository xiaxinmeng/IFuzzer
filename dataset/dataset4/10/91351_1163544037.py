
import socket, gc

class Cycle:
    pass

def main():
    c = Cycle()
    c.cycle = c
    c.s = socket.socket()

    del c
    # import any module that hasn't been imported yet to trigger the bug
    import base64

main()
