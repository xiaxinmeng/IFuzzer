# Demonstrate list mutation during iteration
# Infinite loop that overflows memory
s = [None]
for x in s:
   s.append(x)