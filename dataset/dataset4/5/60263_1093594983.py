import md5
# Start hash generation
m = md5.new()
m.update("Content")

# Serialize m
serialized_m = serialize(m)

# In another function/machine, deserialize m
# and continue hash generation
m2 = deserialize(serialized_m)
m2.update("More content")
m2.digest() 