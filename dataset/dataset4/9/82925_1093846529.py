with Pool() as pool:
    pool.map(sleep, [0.01] * 10)