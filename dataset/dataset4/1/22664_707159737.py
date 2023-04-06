
BPF = 56   
RECIP_BPF = 2 ** -BPF
def random(self):
        """Get the next random number in the range [0.0, 1.0)."""
        return int.from_bytes(_urandom(7), 'big') * RECIP_BPF
