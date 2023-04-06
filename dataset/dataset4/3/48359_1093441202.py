def test():
    code=''
    def sub(n):
        for i in range(n):
            code+=str(i)
    sub(5)
    sub(10)
    return code