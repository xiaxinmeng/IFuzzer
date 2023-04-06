# import ast
import itertools




def find_node_for_range(varlist,trange):
	rangenode = {}
	for item in trange.keys():
		name = item[0]
		lineno = item[1]
		col_offset= item[2]
		mark = item[3]
		startPos = int(trange[item][0])
		endPos = int(trange[item][1])
		key = (name,lineno,col_offset,mark,startPos,endPos)
		rangenode[key] = set()
		for var in varlist:
			varlineno = var[1]
			if varlineno >= startPos and varlineno < endPos + 1:
				rangenode[key].add(var)
	return rangenode



def gen_candidate(funcnode,classnode,varlist):
	allnode = {}
	candict = {}
	allcandidate = set(varlist)
	if funcnode:
		allnode.update(funcnode)
		for func in funcnode:
			candict[func] = allcandidate
	if classnode:
		allnode.update(classnode)
		for cla in classnode:
			candict[cla] = allcandidate


	candict[('global',0,10000,"global",0,10000)]= allcandidate

	for node in candict:
		startPos = node[4]
		endPos = node[5]
		for n in candict:
			nstart = n[4]
			nend = n[5]
			if startPos < nstart and endPos >= nend:
				candict[node] = candict[node] - allnode[n]
			elif startPos < nstart and endPos < nend:
				candict[node] = candict[node] - allnode[n]
				candict[n] = candict[n] - allnode[node]



	return candict



def gen_hole(funcnode,classnode,varlist):
	allnode = {}
	candict = {}
	allcandidate = set(varlist)
	if funcnode:
		allnode.update(funcnode)
		for func in funcnode:
			candict[func] = funcnode[func]
	if classnode:
		allnode.update(classnode)
		for cla in classnode:
			candict[cla] = classnode[cla]


	candict[('global',0,10000,"global",0,10000)]= allcandidate

	for node in candict:
		startPos = node[4]
		endPos = node[5]
		for n in candict:
			nstart = n[4]
			nend = n[5]
			if startPos < nstart and endPos >= nend:
				candict[node] = candict[node] - allnode[n]
			elif startPos < nstart and endPos < nend:
				candict[node] = candict[node] - allnode[n]
				candict[n] = candict[n] - allnode[node]



	return candict







def scope_partition(varlist,funcRange,classRange):
	funcnode = find_node_for_range(varlist,funcRange)
	# print(funcnode)
	classnode = find_node_for_range(varlist,classRange)
	candidict = gen_candidate(funcnode,classnode,varlist)
	# for item in candiset:
	# 	print(item,"......",candiset[item])


	holedict = gen_hole(funcnode,classnode,varlist)
	# for item in holeset:
	# 	print(item,"......",holeset[item])


	return candidict,holedict




def ToListSet(iterable):
    rlist = []
    # print(iterable)
    # print(list(iterable))
    for item  in iterable:
    # print(k)
        # print("ooooo")
        # print(k[0])
        # print(k[1])
        slist = []
        for k in item:

            if isinstance(k,list):
                slist =slist + k
            else:
                slist.append(k)
        rlist.append(slist)


    # print(rlist)
    return rlist



def fillhole(candidict,holedict):
	combinations = []
	scope = []
	for holes in holedict.keys():
		# print(holes)
		if holedict[holes]:
			cset = set()
			for item in candidict[holes]:
				cset.add(item[0])
			

			combination = ToListSet(itertools.product(cset, repeat=len(holedict[holes])))
			# print(combination)
			if combinations:

				combinations =  ToListSet(itertools.product(combinations,combination))
			else:	
				combinations = combination
			scope.append(holes)
	return combinations,scope
