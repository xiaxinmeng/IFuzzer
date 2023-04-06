
for each in __builtin__.__dict__:
    try:
        obj = getattr(__builtin__, each)
        if not callable(obj): 
            continue
        inspect.getfullargspec(obj)
    except Exception as e:
        print(each, e)
