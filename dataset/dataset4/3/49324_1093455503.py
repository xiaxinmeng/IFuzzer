import ctypes

b = ctypes.windll.Kernel32
var1 = 'TEMP'
out = ctypes.create_string_buffer(40) 
c = b.GetEnvironmentVariableW(var1,out,40)
print('ones', c, out, out.raw)
print('two: ', dir(out))