if a_key < b_key:
    yield a_tuple
    try:
        a_value, a_key = a_tuple = next_a()
    except StopIteration:
        yield b_tuple
        yield from b_iter
        return