def fail1():
    try:
        raise RuntimeError('First')
    except:
        fail2()
        raise

fail1()