import lzma
from functools import partial
import multiprocessing

def run_lzma(data,c):
    return c.compress(data)


def split_len(seq, length):
    return [str.encode(seq[i:i+length]) for i in range(0, len(seq), length)]



sequence='AAAAAJKDDDDDDDDDDDDDDDDDDDDDDDDDDDDGJFKSHFKLHALWEHAIHWEOIAH IOAHIOWEHIOHEIOFEAFEASFEAFWEWWWWWWWWWWWWWWWWWWWWWWWWWWWWWEWFQWEWQWQGEWQFEWFDWEWEGEFGWEG'
threads=3
blocksize = int(round(len(sequence)/threads))
strings = split_len(sequence, blocksize)