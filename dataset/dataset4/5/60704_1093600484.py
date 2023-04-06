for hook in hooks:
    try:
        hook()
    except:
        try:
            sys.excepthook(*sys.exc_info())
        except:
            pass