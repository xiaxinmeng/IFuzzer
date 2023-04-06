
import sys

total_size = 0
num_dicts = 1_000 # number of dicts with len(d) == 1
for len_dict in range(1, 2000):
    d = dict.fromkeys(range(len_dict))
    total_size += sys.getsizeof(d) * num_dicts
    num_dicts = round(num_dicts * 0.98)  # geometric distribution
print(f'{total_size:,}')
