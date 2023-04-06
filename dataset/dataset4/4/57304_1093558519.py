def unique_list(seq): # Dave Kirby
    # Order preserving
    seen = set()
    return [x for x in seq if x not in seen and not seen.add(x)]
    
def merge_list(seq):
    merged = []
    for s in seq:
        for x in s:
            merged.append(x)
    return merged