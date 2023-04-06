def greenlet_spawn(fn, *args, **kwargs):

    # spawning a greenlet is necessary
    context = greenlet.greenlet(fn, greenlet.getcurrent())

    # assignment to "result" is necessary
    result = context.switch(*args, **kwargs)