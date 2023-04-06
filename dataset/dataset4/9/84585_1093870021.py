mapping = {fut: index for fut, index in enumerate(futures)}
for fut in as_completed(mapping):
  mapping[fut]  # KeyError