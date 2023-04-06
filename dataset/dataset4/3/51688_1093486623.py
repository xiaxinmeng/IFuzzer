from itertools import tee, chain, islice, groupby
from heapq import merge

def hamming_numbers(shorthand = False):

    def deferred_output():
        for i in output:
            yield i