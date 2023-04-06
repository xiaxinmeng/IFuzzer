
import array
import heapq
import random

a = array.array('I', (random.randrange(10) for _ in range(10)))
heapq.heapify(a)
