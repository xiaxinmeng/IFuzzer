# Desired safe string to expect
goodString = "f42e6be1-29bf-4f3c-ba58-1ae1d9ca5f88"

# Test string to return False if it's not within reg ex range.
# but still returns a false positive even though the g at the start is outside of a-f range.
badString = "g42e6be1-29bf-4f3c-ba58-1ae1d9ca5f88"

# 2nd test string which does return a false result correctly.
otherBadString = "fg2e6be1-29bf-4f3c-ba58-1ae1d9ca5f88"