
def g():
    for _ in range(3):
        try:
            return _
        finally:
            try:
                return_
            finally:
                break
g()
