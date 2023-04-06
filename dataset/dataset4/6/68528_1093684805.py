def g():
    try: pass
    except ImportError as e: pass
    try: pass
    except ImportError as e: pass
    try: pass
    except ImportError as e: pass
    try: pass
    except ImportError as e: pass
    try: pass
    except ImportError as e: pass
    try: pass
    except ImportError as e: pass
print(g.__code__.co_stacksize)