from functools import wraps, partial
def never_throw(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        try: return f(*args, **kwargs)
        except: pass
    return wrapper 