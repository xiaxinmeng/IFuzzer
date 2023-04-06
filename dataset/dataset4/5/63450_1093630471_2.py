def __mix_single_column(self, a):
    a ^= a ^ xtime(a ^ (a[1:] + a[0:1]))