import sys
sys.path.insert(0, '/home/stefan/tmp')
print(sys.path)

distutils_all = ['xyz']
__import__('distutils.command',globals(),locals(),distutils_all)