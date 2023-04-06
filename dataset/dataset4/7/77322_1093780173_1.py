class D:
	def __set_name__(self, o, n):
		self.name = n

class C:
	d: int = D()

if __name__ == "__main__":
	print(f"C.d.name = {C.d.name}") # __set_name__ was called
	assert inspect.ismethoddescriptor(C.d) # Error