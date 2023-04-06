import re

inner = 'VARCHAR(30) COLLATE "en_US"'

result = re.sub(
    r'((?: COLLATE.*)?)$',
    r'FOO\1',
    inner
)

print(inner)
print(result)