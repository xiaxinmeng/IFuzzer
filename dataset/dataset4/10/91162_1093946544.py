def return_first(tup: tuple[int, ...]) -> int:
    return tup[0]
tup: tuple[()] = ()
return_first(tup)