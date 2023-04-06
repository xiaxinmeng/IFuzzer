def test():
    my_list = ["value2", "value3"]
    yield "value1", *my_list
    return "value1", *my_list