population = list(range(10))
weights = list(-1 * w for w in range(10))
[random.choices(population, weights) for _ in range(1000)]