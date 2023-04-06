with ExitStack() as stack:
    if condition:
        stack.enter_context(transaction)
    ...