def hook(args):
    if args.exc_type == SystemExit:
        return
    sys.excepthook(args.exc_type, args.exc_value, args.exc_traceback)

threading.excepthook = hook