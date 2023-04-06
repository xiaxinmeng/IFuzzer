old_size = thread.get_stacksize()
thread.set_stacksize(new_size)
...
thread.set_stacksize(old_size)