def test(v1):
    print(v1)
    print("Before exec(): " + str(locals()))
    exec(v1)
    print("After  exec(): " + str(locals()))
#   This fails:
#    print(u)
#   This is workaround:
    en = locals()['u']
    print(en)

v1="u=4"
test(v1)