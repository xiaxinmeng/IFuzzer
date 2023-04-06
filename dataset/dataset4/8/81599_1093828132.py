def my_decorator(f):
	print("before")
	f()
	print("after")


@my_decorator
def my_function():
	print("hello world")