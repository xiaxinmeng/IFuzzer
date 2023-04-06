while True:
   fail=failureObject()
   for x in ["data1", "data2"]:
       checkAlive(fail, x)
   print(fail.status())