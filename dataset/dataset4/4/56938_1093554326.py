tucs2 = 'A\U0001043cBC\U0001042f\U00010445DE\U00010428H'
tutf16= UTF16(tucs2)
tlist = ['A', '\U0001043c','B','C','\U0001042f','\U00010445',
         'D','E','\U00010428','H']
tlis2 = [tutf16[i] for i in range(len(tlist))]
assert tlist == tlis2