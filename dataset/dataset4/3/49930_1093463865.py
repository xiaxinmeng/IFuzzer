import sys
# ...
if __name__ == '__main__':
    if 'idlelib.PyShell' in sys.modules:
        sys.argv.extend(('a', '-2'))  # add your argments here.
    print(sys.argv)  # in use, parse sys.argv after extending it
    # ['C:\\Programs\\python34\\tem.py', 'a', '-2']