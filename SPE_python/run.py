import datetime
import os

# tdir = '/home/xxm/Desktop/IFuzzer/IFuzzer1.0/SPE/SPE_python/dataset/dataset1_2/gpython'
# tdir = '/home/xxm/Desktop/IFuzzer/IFuzzer1.0/SPE/SPE_python/dataset/dataset1_2/hython'
# tdir = '/home/xxm/Desktop/IFuzzer/IFuzzer1.0/SPE/SPE_python/dataset/dataset1_2/IronPython'
# tdir = '/home/xxm/Desktop/IFuzzer/IFuzzer1.0/SPE/SPE_python/dataset/dataset1_2/jython'
# tdir = '/home/xxm/Desktop/IFuzzer/IFuzzer1.0/SPE/SPE_python/dataset/dataset1_2/jython1'
# tdir = '/home/xxm/Desktop/IFuzzer/IFuzzer1.0/SPE/SPE_python/dataset/dataset1_2/jython2'
# tdir = '/home/xxm/Desktop/IFuzzer/IFuzzer1.0/SPE/SPE_python/dataset/dataset1_2/pypy'
# tdir = '/home/xxm/Desktop/IFuzzer/IFuzzer1.0/SPE/SPE_python/dataset/dataset1_2/pypy1'
# tdir = '/home/xxm/Desktop/IFuzzer/IFuzzer1.0/SPE/SPE_python/dataset/dataset1_2/rustPython'
# tdir = '/home/xxm/Desktop/IFuzzer/IFuzzer1.0/SPE/SPE_python/dataset/dataset1_2/rustPython1'
# tdir = '/home/xxm/Desktop/IFuzzer/IFuzzer1.0/SPE/SPE_python/dataset/dataset1_2/rustPython2'
# tdir = '/home/xxm/Desktop/IFuzzer/IFuzzer1.0/SPE/SPE_python/dataset/dataset1_2/withFunc'
# tdir = '/home/xxm/Desktop/IFuzzer/IFuzzer1.0/SPE/SPE_python/dataset/dataset1_2/withFunc1'
# tdir = '/home/xxm/Desktop/IFuzzer/IFuzzer1.0/SPE/SPE_python/dataset/dataset1_2/withFunc2'
# tdir = '/home/xxm/Desktop/IFuzzer/IFuzzer1.0/SPE/SPE_python/dataset/dataset1_2/withoutFunc'
tdir = '/home/xxm/Desktop/IFuzzer/IFuzzer1.0/SPE/SPE_python/dataset/dataset1_2/withoutFunc1'
 

# tdir = '/home/xxm/Desktop/IFuzzer/IFuzzer1.0/SPE/SPE_python/dataset/dataset2/aaa1'
# tdir = '/home/xxm/Desktop/IFuzzer/IFuzzer1.0/SPE/SPE_python/dataset/dataset2/aaa2'
# tdir = '/home/xxm/Desktop/IFuzzer/IFuzzer1.0/SPE/SPE_python/dataset/dataset2/aaa3'
# tdir = '/home/xxm/Desktop/IFuzzer/IFuzzer1.0/SPE/SPE_python/dataset/dataset2/aaa4'
# tdir = '/home/xxm/Desktop/IFuzzer/IFuzzer1.0/SPE/SPE_python/dataset/dataset2/aaa5'
# tdir = '/home/xxm/Desktop/IFuzzer/IFuzzer1.0/SPE/SPE_python/dataset/dataset2/aaa6'
# tdir = '/home/xxm/Desktop/IFuzzer/IFuzzer1.0/SPE/SPE_python/dataset/dataset2/aaa7'
# tdir = '/home/xxm/Desktop/IFuzzer/IFuzzer1.0/SPE/SPE_python/dataset/dataset2/aaa8'
# tdir = '/home/xxm/Desktop/IFuzzer/IFuzzer1.0/SPE/SPE_python/dataset/dataset1_1'


# tdir =  '/home/xxm/Desktop/IFuzzer/IFuzzer1.0/SPE/SPE_python/dataset/dataset0'



for root,dirs, files in os.walk(tdir):
	for file in files:
		# print(root,file)
		path = root+ "/"+file
		os.system("python3 'runsinglefile.py' %s"%path)


print("All finish...........")
