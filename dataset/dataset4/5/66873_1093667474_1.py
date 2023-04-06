from bisect import bisect_left

a = [1, 2, 3, 4]
idx = bisect_left(a, 2, 0, 10)  # 10 > 2 * 4
print(idx)