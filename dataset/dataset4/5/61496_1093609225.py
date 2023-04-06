def ee_compile(code, src=''):
    try:
        return compile(code, src, 'eval')
    except SyntaxError:
        return compile(code, src, 'exec')  # or 'single' would work

a = eval(ee_compile('1+1'))
b = eval(ee_compile('c = 3'))
print(a, b, c)
# 2 None 3