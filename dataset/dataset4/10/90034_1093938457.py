for i in range(10_000_000):
    numerator: int = randrange(10 ** randrange(40)) + 1
    denonimator: int = randrange(10 ** randrange(40)) + 1
    x: Fraction = Fraction(numerator, denonimator)