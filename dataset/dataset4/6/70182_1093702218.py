def g():
    try:
        yield "item"
    finally:
        # Run at exhaustion, close(), and garbage collection
        print("finally")

gi = g()
try:
    item = next(gi)
    print(item / 2)  # Oops, TypeError
finally:
    # Should be run as the exception passes through. GeneratorExit is raised inside the generator, causing the other “finally” block to execute. All before the original exception is caught and a traceback is printed.
    gi.close()