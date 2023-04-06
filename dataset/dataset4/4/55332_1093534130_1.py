# Invert a table (this is again totally general).
# All keys of the original table are made keys of the inverse,
# so there may be empty lists in the inverse.
#
def inverse(table):
    inv = {}
    for key in table.keys():
        if not inv.has_key(key):
            inv[key] = []
        for item in table[key]:
            store(inv, item, key)
    return inv