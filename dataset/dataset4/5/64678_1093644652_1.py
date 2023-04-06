def mean(data, weights=None):
    if weights is not None:
        return mean(flatten([x]*w for x, w in zip(data, weights)))
    # base case without weights is unchanged