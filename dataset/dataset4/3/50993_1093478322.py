from select import kevent

if __name__ == '__main__':
    ev = kevent(1)
    print(repr(ev))