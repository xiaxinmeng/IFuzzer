my_iterable = ...

with ProcessPoolExecutor() as executor:
    def process_item(item):
        ...
        return result
    results = executor.map(process_item, my_iterable)

# do sth with results