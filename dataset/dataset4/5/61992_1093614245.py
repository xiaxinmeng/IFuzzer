def bad():
    e = None
    try:
        do_something()
    except KeyError as e:
        print('ke')
    except ValueError as e:
        print('ve')
    print(e)