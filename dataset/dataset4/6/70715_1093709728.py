def run(**kwargs):
    g = event_gen(**kwargs)
    r = next(g)
    g.close()
    r()