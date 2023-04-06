import time

def create_generator():
    try:
        yield
    finally:
        time.sleep(2)

ct = create_generator()
ct.next()