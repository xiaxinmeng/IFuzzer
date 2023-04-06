
def loop():
    a_node = boost_python_library.get_linked_list()
    all_elems = []
    while a_node is not None:
        #
        # Uncomment the below to make the crash disappear
        #
        # all_elems.append(a_node)
        #
        a_node = a_node.next
