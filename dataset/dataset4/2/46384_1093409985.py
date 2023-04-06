#buggy unicode support module:
import codecs
filewr=codecs.open('myfile.txt','w','utf-8')
filewr.write("abc"+"\n")