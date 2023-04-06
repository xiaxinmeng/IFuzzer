def random_subset_with_counts(sequence, counts):
    result = []
    for x, k in zip(sequence, counts):
        result.extend([x] * random.getrandbits(k).bit_count())
    return result