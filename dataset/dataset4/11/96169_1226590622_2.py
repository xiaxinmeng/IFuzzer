class Random_bit_length(random.Random):
    def _randbelow(self, n):
        "Return a random int in the range [0,n).  Defined for n > 0."

        k = n.bit_length()
        # 0 <= r < 2**k
        while (r := self.getrandbits(k)) >= n:
            pass
        return r