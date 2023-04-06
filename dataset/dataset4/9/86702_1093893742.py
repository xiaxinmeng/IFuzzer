container = []
iterator = zip([container], [container])

# untrack the internal zip->result=(None, None)
gc.collect()

# create a reference cycle: container -> iterator -> container
container.append(iterator)

next(iterator)
# zip->result=(container, container)