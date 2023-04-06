from socket import *
from struct import *
s = socket(AF_IRDA, SOCK_STREAM)
info = s.getsockopt(SOL_IRLMP, IRLMP_ENUMDEVICES, 1024)
list = info[4:]
list
addr = unpack('I', list[:4])[0]
s.connect((addr, "IrDA:IrCOMM"))
s.close()