
sorted(a_dict.keys() | {'missing', 'data'})
sorted(set(a_dict) | {'missing', 'data'})
sorted([*a_dict, 'missing', 'data'])
sorted({*a_dict, 'missing', 'data'})
