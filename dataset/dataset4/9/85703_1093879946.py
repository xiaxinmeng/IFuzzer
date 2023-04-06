import sys
LEN = int(sys.argv[1])

with open('big_dict.py', 'w') as f:
    print('INTS = {', file=f)
    for i in range(LEN):
        print(f'    {i}: None,', file=f)
    print('}', file=f)


import big_dict
assert len(big_dict.INTS) == LEN, len(big_dict.INTS)