def test():
    import yum
    # work with yum

test()
gc.collect() # to sure that nothing have extra references.
# yum logs still alive in spite of that yum module (and imported logging module) 'is unloaded'