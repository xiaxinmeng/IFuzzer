def set_intersection_sorted(*input_sets):
    input_sets = sorted(input_sets, key=len)
    new_set = set()
    for element in input_sets[0]:
        if element in input_sets[1]:
            if element in input_sets[2]:
                new_set.add(element)
    return new_set