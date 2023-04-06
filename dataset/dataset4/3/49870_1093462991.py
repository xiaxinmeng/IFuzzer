class C1:
	myurl = []	
	def test(self):
		url = [5,6,7]
		self.myurl.extend(url)		
def testv():
	c = C1()
	c.test()
	print(c.myurl)
	
i = 0
while i<10 :
	testv()
	i = i+1