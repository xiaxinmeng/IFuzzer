class BSTR(_SimpleCData):
    _type_ = "X"

func = oledll.oleaut32.SysStringLen
func.argtypes = (BSTR,)

while 1:
    func("abcdefghijk")