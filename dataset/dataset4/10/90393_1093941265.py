from pyperf import Runner
runner = Runner()

for n in [2, 10, 100, 10_000]:
    for A in [
        '[None]',
        '["Python", "Perl"]',
        'list(range(10))',
        'list(range(100))',
        'list(range(1000))',
        '(None,)',
        '("Python", "Perl")',
        'tuple(range(10))',
        'tuple(range(100))',
        'tuple(range(1000))',
    ]:
        runner.timeit(    
            name=f"{A} * {n}",
            setup=f"x = {A}",
            stmt=f"x * {n}",
        )