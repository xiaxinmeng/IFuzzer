from queue import Empty, PriorityQueue

def test(qcls):
    q = qcls()
    for i in inp:
        q.put(i)
    out = []
    try:
        while True:
            out.append(q.get(timeout=1))
    except Empty:
        pass
    plt.plot(out)
    plt.show()

test(PriorityQueue)