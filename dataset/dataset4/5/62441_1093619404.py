def uniqueheappush(heap, inheap, item):
    if id(item) in inheap:
        return False
    heappush(heap, item)
    inheap.add(id(item))
    return True

def uniqueheappop(heap, inheap):
    item = heappop(heap, inheap)
    inheap.discard(id(item))
    return item