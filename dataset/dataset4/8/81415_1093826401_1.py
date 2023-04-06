def test(t):
	n = 0
	def f(t):
		N = n+1
		print(t+str(N))
	f(t)	
test('test')