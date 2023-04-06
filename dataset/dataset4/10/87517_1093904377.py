
def loop():
    a_node = boost_python_library.get_linked_list()
    temp = []
    while True:
        assert a_node is not None
        temp.append(a_node)
        prev = a_node   # <-- comment this out to make the crash go away
        a_node = a_node.next
        if not a_node:
            break
