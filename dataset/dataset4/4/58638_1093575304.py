pycon
"""
>>> import os
[67212 refs]
>>> stdin = os.fdopen(0)
[67234 refs]
>>> del stdin
__main__:1: ResourceWarning: unclosed file <_io.TextIOWrapper name=0 mode='r' encoding='UTF-8'>
[67260 refs]
>>> 
[67261 refs]
[44710 refs]
"""
