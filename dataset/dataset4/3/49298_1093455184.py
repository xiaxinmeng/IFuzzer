max((comb for comb in all_combinations(zip(weights, values))
       if sum(map(itemgetter(0), comb)) < LIM), 
     key=lambda comb: sum(map(itemgetter(1), comb)))