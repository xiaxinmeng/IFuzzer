ges = [o for o in gc.get_objects() if isinstance(o, GeneratorExit)]
if ges:
    ge, = ges
    print(gc.get_referrers(ge))