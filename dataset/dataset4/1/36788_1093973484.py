import imp,sys,string
magic = string.join(["\\x%.2x" % ord(c) for c in
imp.get_magic()],"")
reg = ':pyc:M::%s::%s:' % (magic, sys.executable)
open("/proc/sys/fs/binfmt_misc/register","wb").write(reg)