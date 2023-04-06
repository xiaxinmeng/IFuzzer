from pyperf import Runner
runner = Runner()

runner.timeit(
    "float_loop",
    setup="arr = [float(x) for x in range(5_000_000)]",
    stmt="for x in arr:\n"
         "    if x > 1e6:\n"
         "        break\n",
)

runner.timeit(
    "int_loop",
    setup="arr = list(range(5_000_000))",
    stmt="for i in arr:\n"
         "    if i == 6_000_000:\n"
         "        break\n",
)

runner.timeit(
    "str_loop",
    setup="arr = ['Py'] * 5_000_000",
    stmt="for word in arr:\n"
         "    if word == 'Python':\n"
         "        break\n",
)

"""
float_loop: Mean +- std dev: [compare_before] 17.7 ms +- 0.3 ms -> [compare_after] 14.3 ms +- 0.1 ms: 1.24x faster
int_loop: Mean +- std dev: [compare_before] 87.7 ms +- 1.4 ms -> [compare_after] 74.7 ms +- 1.2 ms: 1.17x faster
str_loop: Mean +- std dev: [compare_before] 85.3 ms +- 4.5 ms -> [compare_after] 70.2 ms +- 2.6 ms: 1.21x faster

Geometric mean: 1.21x faster
"""