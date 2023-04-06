from timeit import timeit
timeit("print('nnn '*500)", number=10)  # Exp1: .0357, .0355
timeit("for i in range(500): print(i)", number=4)  # Exp2: 1.45, 1.70
timeit("print(*range(500))", number=4)  # Exp3: about 5*, 4.85