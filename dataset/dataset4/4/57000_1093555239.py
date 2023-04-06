def leaky_generator():
    try:   
        1/0
    except:  # Exception handler with anonymous exception variable
        try:
            yield  # Yield from exception handler
        except (GeneratorExit, RuntimeError):
            pass

def throw_leaks(g):
    try:
        g.throw(RuntimeError())
    except Exception:
        pass