source = """
try:
    try:
        TRY_BLOCK
    except EXC1:
        EXC_BLOCK1
    except EXC2:
        EXC_BLOCK1
except EXC3:
    FIN_BLOCK
"""

import parser
stlist = parser.suite(source).tolist()  # o.k.
parser.sequence2st(stlist)