
def foo(c):
         try:
             c = c + 1
             print("ss"+str(c))
             foo(c)
         except Exception as e:
             print(str(e) + " -- " + str(c))
             print("kk")
         print(c)
c = 0
foo(c)
