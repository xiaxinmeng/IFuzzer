def product2(*args, repeat=1):
    def concat(result, pool):
        yield from (x+[y] for x in result for y in pool)
        
    pools = [tuple(pool) for pool in args] * repeat
    result = [[]]
    for pool in pools:
        result = concat(result, pool)
    for prod in result:
        yield (tuple(prod))