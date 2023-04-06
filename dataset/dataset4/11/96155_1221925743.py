def polynomial_from_roots(roots):
    poly = [1]
    for root in roots:
        poly = [a + b for a, b in zip([0] + [c * -root for c in poly], poly + [0])]
    return poly