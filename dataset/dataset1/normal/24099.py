import heapq as h

class X():
  def __lt__(self, o):
    global L

    n = len(L)
    print("len(L):", n)
    for i in range(n):
      del L[0]
      L.append(X())
    return 1

L = []
for i in range(2):
  h.heappush(L, X())

print(L)
