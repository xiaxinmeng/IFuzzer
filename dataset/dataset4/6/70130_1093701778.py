with Popen(...) as p:
    return p.wait()
    # If interrupted, the context manager will wait again. If the interruption is due to a terminal-wide SIGINT, the child may also have been interrupted.