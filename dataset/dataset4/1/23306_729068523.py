import timeit
timeit.timeit(stmt="rgb_to_hls(255, 255, 255)", setup="from colorsys import rgb_to_hls")