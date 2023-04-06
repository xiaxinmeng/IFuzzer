# list of tuples in form of (priority_number, data)
bugged = [
(-25.691, {'feedback': 13, 'sentiment': 0.309, 'support_ticket': 5}), (-25.691, {'feedback': 11, 'sentiment': 0.309, 'support_ticket': 3}), (-25.0, {'feedback': 23, 'sentiment': 0.0, 'support_ticket': 15}),
]

from queue import PriorityQueue

pq = PriorityQueue()

for item in bugged:
   pq.put(item)