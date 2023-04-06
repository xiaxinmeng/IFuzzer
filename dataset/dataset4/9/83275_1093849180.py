sentinel = objet()
avg = mean(data, default=sentinel)
if avg is sentinel:
   ... # special code path