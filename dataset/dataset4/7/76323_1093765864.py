import heapq
li = [5, 7, 9, 1, 4, 3]
heapq.heapify(li)
#change a couple values in the heap
li[3] = 16
li[4] = 2
print (heapq.heappop(li))
print ("The heap after pop is : ",end="")
print (list(li))