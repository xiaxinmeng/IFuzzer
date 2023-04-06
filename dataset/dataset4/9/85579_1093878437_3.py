class my_map:
    def __init__(self, mapping_function, *iterators):
        self.mapping = mapping_function
        self.iterators = iterators
    
    def __iter__(self):
        for parameter_tuple in zip(*self.iterators):
            try:
                yield self.mapping(*parameter_tuple)
            except BaseException as e:
                raise RuntimeError(*e.args) from e
        
# It works like the map in most cases:

print('example 3'.center(30, '='))
for item in my_map(raise_stop_iteration, range(5)):
    print(item)
print('end of example 3'.center(30, '='))

# And then, the crash of the buggy mapping function will be reported:
print('example 4'.center(30, '='))
for item in my_map(raise_stop_iteration, range(10, 20)):
    print(item)
print('end of example 4'.center(30, '='))