class MiniContext():
    def __init__(self):
        pass

    def __enter__(self):
        print('Hello')

    def __exit__(self, *args):
        print('Goodbye')

def gen():
	with MiniContext():
		yield 1

print(next(gen()))