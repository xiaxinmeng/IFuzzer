def thread(func):
    """

    """
    def wrapper(*args, **kwargs) -> Thread:
        t = Thread(target=func, args=args, kwargs=kwargs)
        t.start()
        return t
    
    return wrapper