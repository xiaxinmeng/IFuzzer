def getmaxyx(self):
    # taken from http://dag.wieers.com/home-made/dstat/
    try:
        h, w = int(os.environ["LINES"]), int(os.environ["COLUMNS"])
    except KeyError:
        try:
            h, w = curses.tigetnum('lines'), curses.tigetnum('cols')
        except:
            try:
                s = struct.pack('HHHH', 0, 0, 0, 0)
                x = fcntl.ioctl(sys.stdout.fileno(), termios.TIOCGWINSZ,
s)
                h, w = struct.unpack('HHHH', x)[:2]
            except:
                h, w = 25, 80