def ab_combinations():
    #'', 'a', 'b', 'aa', 'ab', 'ba', 'bb', 'aaa', ...
    def _deferred_output():
        yield ""
        tees = tee(output)

        #This definition works fine: '', 'a', 'b', 'aa', 'ab', 'ba', ...
        l = [(item+"a" for item in tees[0]), (item+"b" for item in tees[1])]

        #This definition results in: '', 'b', 'b', 'bb', 'bb', 'bb', ...
        #l = [(item+label for item in t) for t, label in zip(tees,"ab")]
        
        while True:
            for g in l:
                yield next(g)