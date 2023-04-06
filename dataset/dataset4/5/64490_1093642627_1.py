def sumseq(seq, a=0, b=None):
    # Pure python code with nullable int
    if b is None:
        b = len(seq)
    return sum(seq[a:b])