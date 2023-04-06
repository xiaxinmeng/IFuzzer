
lookup()
if not collision:
    return result

while True:
    perturb_shift()
    lookup()
    if not collision:
        return result
