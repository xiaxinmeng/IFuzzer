
# referrers.py
import gc, sys

class FakeMod(object): pass

extra = []

def test():
    mod = FakeMod()
    extra.append(mod)
    referrers = gc.get_referrers(mod)
    print(".".join(str(x) for x in sys.version_info[:3]), ":", len(referrers), referrers)

test()
