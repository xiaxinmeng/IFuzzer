def test():
   for abc in range(10):
       try: pass
       finally:
           try:
               continue
           except:
               pass