# Since there's no list.find(), this is my workaround to achieve making only one linear search per query
def find(container: list, index: int) -> int:
    """ Str.find() behavior but for lists """
    try:
        return container.index(index)
    except ValueError:
        return -1

# Example driver code:
index = find(list, possible_element)
if index_of_element == -1:
    pass # Not found
else:
    pass # Found