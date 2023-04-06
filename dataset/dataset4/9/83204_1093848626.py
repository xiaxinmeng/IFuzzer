#!/usr/bin/env python3
import random
lis = '94'
random.seed(lis, version=1)
w = random.random() * 100
print('rand string seed: %d' % w)
lis = 94
random.seed(lis, version=1)
w = random.random() * 100
print('rand int seed: %d' % w)