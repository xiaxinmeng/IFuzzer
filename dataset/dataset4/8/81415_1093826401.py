def test(t):
	n = 0
	def f(t):
		n = n+1
		print(t+str(n))
	f(t)	
test('test')	