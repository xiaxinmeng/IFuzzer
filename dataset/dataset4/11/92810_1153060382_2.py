if cls.__name__=="Foobar":
    pass
else:
    print(f"{cls.__name__} has {len(cls.__subclasses__())} subclasses")