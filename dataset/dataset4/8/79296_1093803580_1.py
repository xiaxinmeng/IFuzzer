
import uuid

value = uuid.UUID()

# uuid instances already have the correct value stored in the `.hex` attribute
value.hex

# this raises `TypeError: 'UUID' object cannot be interpreted as an integer`
hex(value)

# this behaves correctly
hex(value.int)

