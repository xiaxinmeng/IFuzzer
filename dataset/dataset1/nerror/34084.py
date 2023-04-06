import inspect
CO_FUTURE_BARRY_AS_BDFL = 0x40000
flags = CO_FUTURE_BARRY_AS_BDFL
code = "print(1 <> 2)"
try:
    compile(code, "filename", "exec", flags=0)
except SyntaxError:
    print("ok")
else:
    raise Exception("SyntaxError expected")
compile(code, "filename", "exec", flags=flags)
print("ok")
