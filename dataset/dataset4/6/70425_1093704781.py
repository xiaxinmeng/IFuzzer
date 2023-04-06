def test():
    try:
        raise Exception('a')
    except Exception as e:
        pass
    else:
        return
    print(e)

test()