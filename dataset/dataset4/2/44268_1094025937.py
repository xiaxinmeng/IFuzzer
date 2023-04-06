for o, a in opts:
    if o == "-v":
        verbose = True
    elif o in ("-h", "--help"):
        usage()
        sys.exit()
    else:
        raise AssertionError(
    "Unparsed Paremter: %s %s" %(o, a))