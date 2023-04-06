if 1:
    def Slow():
        global Slow
        class  Slow:
            global slow
            def slow(self): return self
        return Slow
    if  Slow():
        class Fast:
            global fast
            def fast(self): return self
    import dis
    dis.show_code(slow)
    print()
    dis.show_code(fast)