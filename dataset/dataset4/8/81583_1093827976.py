
def rec():
    try:
        rec()
    except RecursionError:
        rec()

rec()
