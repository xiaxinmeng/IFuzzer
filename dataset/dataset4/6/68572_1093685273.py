def quick_ratio_ge(self, a, b, threshold):
    return threshold <= 2.0*(len(a))/(len(a)+len(b))