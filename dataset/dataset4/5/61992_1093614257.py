def good():
    exc = None
    try:
        bar(int(sys.argv[1]))
    except KeyError as e:
        print('ke')
        exc = e
    except ValueError as e:
        print('ve')
        exc = e
    print(exc)