
try:
    float('áxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
except:
    from collections import namedtuple
    namedtuple('T', 'f')
