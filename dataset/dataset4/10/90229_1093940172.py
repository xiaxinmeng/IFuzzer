ts = TopologicalSorter()
for u, successors in my_forward_graph.items():
    for v in successors:
        ts.add(v, u)