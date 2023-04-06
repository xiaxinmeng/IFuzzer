q.get(True, 0.5)
# Expected result: block for half a second before throwing exception
# Actual result: throws empty exception immediately without waiting

q.get(True, 1)
# Expected result: block for one second before throwing exception
# Actual result: throws empty exception immediately without waiting

q.get(True, 1.00001)
# Expected result: block for just over a second before throwing exception
# Actual result: throws empty exception immediately without waiting

q.get(True, 1.00002)
# Blocks for just over a second, as expected

q.get(True, 2)
# Blocks for two seconds, as expected