def x():
    try:
        raise Exception()
    except Exception:
        x()