if some_test:
    fl = contextlib.closing(open(sys.argv[1]))
else:
    fl = sys.stdin
with fl as fl:
    do_stuff(fl)