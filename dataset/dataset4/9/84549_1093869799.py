def create_q(l: list[int]) -> Queue[int]:
    q = Queue[int]()
    for e in l:
        q.put(e)
    return q

a = create_q([1,2,3,4,5])