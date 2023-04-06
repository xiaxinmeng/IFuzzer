ts = TopologicalSorter(my_forward_graph).static_order()
ts = reversed(ts)