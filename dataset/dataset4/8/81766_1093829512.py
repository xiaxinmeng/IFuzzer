
my_dict = {'foo': 'bar'}
dict_copy = my_dict.copy()
other_dict = {'foo': 'bar', 'bar': 1234}

assert my_dict.keys() == my_dict.keys()
assert my_dict.keys() == dict_copy.keys()
assert my_dict.keys() != other_dict.keys()

assert my_dict.items() == my_dict.items()
assert my_dict.items() == dict_copy.items()
assert my_dict.items() != other_dict.items()

assert my_dict.values() == my_dict.values()
assert my_dict.values() == dict_copy.values()
assert my_dict.values() != other_dict.values()

