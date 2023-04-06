with sys.stdout if some_test else contextlib.closing(open(sys.argv[1])) as fl:
    do_stuff(fl)