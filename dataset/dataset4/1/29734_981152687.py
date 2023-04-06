from pyperf import Runner
runner = Runner()

runner.timeit(
    "float_loop",
    setup="arr = [float(x) for x in range(5_000_000)]",
    stmt="for x in arr:\n"
         "    if x > 1e6 or x == 1e6 or x < 0.0:\n"
         "        break\n",
)

runner.timeit(
    "int_loop",
    setup="arr = list(range(5_000_000))",
    stmt="for i in arr:\n"
         "    if i > 6_000_000 or i == 6_000_000 or i < 0:\n"
         "        break\n",
)

runner.timeit(
    "str_loop",
    setup="arr = ['Py'] * 5_000_000",
    stmt="for word in arr:\n"
         "    if word == 'Python' or word != 'Py':\n"
         "        break\n",
)

"""
float_loop: Mean +- std dev: [micro_main] 41.5 ms +- 0.4 ms -> [micro_combined3] 23.7 ms +- 0.8 ms: 1.75x faster
int_loop: Mean +- std dev: [micro_main] 202 ms +- 2 ms -> [micro_combined3] 133 ms +- 1 ms: 1.52x faster
str_loop: Mean +- std dev: [micro_main] 140 ms +- 7 ms -> [micro_combined3] 88.1 ms +- 3.9 ms: 1.59x faster

Geometric mean: 1.62x faster
"""
