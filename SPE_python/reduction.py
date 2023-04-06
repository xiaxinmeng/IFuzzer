
#stringlist: [("a",1,2),("v",2,3)]
def strict_growth_string(stringlist):
	stringcode = ""
	stringdic = {}
	growthcode = 0
	for string in stringlist:
		sname = string
		if sname not in stringdic.keys():
			growthcode = growthcode + 1
			stringdic[sname] = growthcode 
		stringcode = stringcode + str(stringdic[sname]) 

	return stringcode


def reduct(namelist):
	reductlist = []

	sgstr = set()
	for item in namelist:
		scode = strict_growth_string(item)
		if scode not in sgstr:
			reductlist.append(item)
			sgstr.add(scode)

	return reductlist


# s = ['a', 'a', 'a', 'a', 'a', 'rs']
# print(strict_growth_string(s))