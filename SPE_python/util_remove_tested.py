import os 


logdir = '/home/xxm/Desktop/IFuzzer/cpython/SPE_python/SPE_python/log/dataset2'
# '/home/xxm/Desktop/IFuzzer/cpython/SPE_python/dataset'
# '/home/xxm/Desktop/IFuzzer/cpython/SPE_python/dataset/dataset2/cPython_test/aaa/test_atexit/temp.py'
#  '/home/xxm/Desktop/IFuzzer/cpython/SPE_python/dataset/dataset2/cPython_test/aaa1/test_codecencodings_kr/test_codecencodings_kr.py' 
# '/home/xxm/Desktop/IFuzzer/cpython/SPE_python/SPE_python/log/dataset2/cPython_test/aaa1/test_compileall/test_bad_args_log.txt' 



for root,dirs,files in os.walk(logdir):
	for file in files:
		filepath = root + "/" + file
		filepath = filepath.replace("_log.txt",".py").replace("SPE_python/log","dataset")
		if os.path.exists(filepath):
			os.remove(filepath)
			print(filepath)
