# Check for GNU dbm
if magic in (0x13579ace, 0x13579acd, 0x13579acf):
    return "dbm.gnu"