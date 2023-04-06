import ast_analysis 
import ast_transform
import SPE_enum
import reduction
import ast
import datetime
import timeout
import os
import sys



@timeout.set_timeout(120,timeout.after_timeout)
def enum(inputfile):

	rootname = inputfile.split("/dataset/")[0]
	dirname = "/".join(inputfile.split("/dataset/")[1].split('/')[:-1])
	fname = inputfile.split(".py")[0].split('/')[-1]
	dirpath = rootname + "/SPE_python/log/"+dirname
	if not os.path.exists(dirpath):
		os.makedirs(dirpath)
	

	logfilename = dirpath + '/'+ fname + "_log.txt"
	if os.path.exists(logfilename):
		os.remove(logfilename)

	logfile = open(logfilename, 'a') 

	logfile.write("Seed file: %s\n"%inputfile)
	print(inputfile)


	f= open(inputfile,'r').read()


	myast = ast.parse(f)
	# print(ast.dump(myast))
	astvisitor = ast_analysis.CellVisitor()
	astvisitor.visit(myast)
	# print(astvisitor.allname)
	# print(astvisitor.callname)
	# print(astvisitor.funcRange)
	# print(astvisitor.classRange)
	# print(astvisitor.attrname)



	var = astvisitor.allname - astvisitor.attrname - astvisitor.callname
	print("var_Num:%s"%len(var))
	logfile.write("var_Num: %s\n"%len(var))
	candidict,holedict = SPE_enum.scope_partition(var,astvisitor.funcRange,astvisitor.classRange)



	# print(candidict)
	# print(holedict)

	avgCandi = 0
	summ = 0
	count = 0
	scope = 0
	for key in candidict.keys():
		scope = scope + 1
		if candidict[key]:
			count = count + 1
		summ = summ + len(candidict[key])
	if count != 0:
		avgCandi = summ/count

	print("Scope_Num:%s"%scope)
	logfile.write("Scope_Num: %s\n"%scope)

	print("Avg_candi:%s"%avgCandi)
	logfile.write("Avg_candi: %s\n"%avgCandi)


	holeNum = 0
	for key in holedict.keys():
		holeNum = holeNum + len(holedict[key])

	print("holeNum:%s"%holeNum)
	logfile.write("holeNum: %s\n"%holeNum)



	combination,scope = SPE_enum.fillhole(candidict,holedict)


	print("Before_reduction: %s\n"%len(combination))
	logfile.write("Before_reduction: %s\n"%len(combination))
	combination =reduction.reduct(combination)
	print("After_reduction: %s\n"%len(combination))
	logfile.write("After_reduction: %s\n"%len(combination))
	# print(combination,scope)



	newcombination = []
	for com in combination:
		i = 0
		newcom = []
		for sc in scope:
			for item in holedict[sc]:
				newitem  = (com[i],item[1],item[2])
				i = i + 1
				newcom.append(newitem)
		newcombination.append(newcom)



	# print(program,'\n')
	return newcombination


@timeout.set_timeout(30,timeout.after_timeout)
def test_file(interpreter, program,sourcepath, j):
#sourcepath = '/home/xxm/Desktop/IFuzzer/pypy/dataset2/cPython_test/aaa/test_aifc/test_aifc.py'
    rt = sourcepath.split("/dataset/")[0]
    dr = "/".join(sourcepath.split("/dataset/")[1].split("/")[:-1])
    fl = sourcepath.split("/dataset/")[1].split('/')[-1]
    # print(rt,dr,fl)
    ## /home/xxm/Desktop/IFuzzer/pypy cPython_test/aaa/crashers bogus_code_obj.py
    rundir = rt + "/dataset/"+dr
    savepath = rundir+"/temp.py"
    open(savepath,'w').write(program)


    s = os.system("cd %s;%s %s"%(rundir, interpreter, savepath ))

    if s !=0 and s!=256:
        name = sourcepath.split(".py")[0].split('/')[-1]
        dirname = rt+"/SPE_python/error/" + dr
        dest = dirname + "/"+ "%s__%s.py"%(str(name),str(j))
        # dirname  = sourcepath.split(".py")[0].split('/')[-2]


        if not os.path.exists(dirname):
            os.makedirs(dirname)


        open( dest,'w').write(program)
        j=j+1
        open('log.txt','a').write("%s_%s=========%s\n"%(name,j,s))

    return j



@timeout.set_timeout(7200,timeout.after_timeout)
def run(inputfile,newcombination):

	# interpreter = '/home/xxm/Desktop/IFuzzer/pypy/pypy3.7-v7.3.5-linux64/bin/pypy3' 

	# j = 0

	# for newcom in newcombination:
	# 	f= open(inputfile,'r').read()
	# 	program = ast_transform.transform(newcom,myast)


	interpreter =  '/home/xxm/Desktop/IFuzzer/IFuzzer1.0/Python-3.9.0/python'



	j = 0
	f= open(inputfile,'r').read()

	j = test_file(interpreter, f,inputfile, j)


	k = 0
	for newcom in newcombination:
		# print(enum)
		k = k + 1
		print("______________")
		print("\n", inputfile,len(newcombination) - k)



		f= open(inputfile,'r').read()
		# os.system("%s %s"%(interpreter, inputfile))

		myast = ast.parse(f)
		# print("!!!")
		program = ast_transform.transform(newcom,myast)

		print(program,"\n","\n","\n")
		
		j = test_file(interpreter, program,inputfile, j)





def run_single_enum(path):
	# path = root+ "/"+file
	# print(path)
	if path.endswith(".py"): 
		filename = path.split(".py")[0].split('/')[-1]
		dirname = path.split(".py")[0].split('/')[-2] 
		# print(path)
		if filename != dirname and filename != "temp":
			# try:
			starttime = datetime.datetime.now()
			# try:
			enumlist = enum(path)
			# print("ss",enumlist)

			
			run(path,enumlist)



			logfilename =path.split("/dataset/")[0]+"/SPE_python/log/"+  "/".join(path.split("/dataset/")[1].split('/')[:-1]) + '/'+ path.split(".py")[0].split('/')[-1] + "_log.txt"
			# print("....................",logfilename)
			endtime = datetime.datetime.now()
			open(logfilename,'a').write("Total time: %s"%(endtime - starttime))
			print((endtime - starttime),"\n")	


