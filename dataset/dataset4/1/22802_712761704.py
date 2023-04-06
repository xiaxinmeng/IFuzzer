def test_42057():
    for i in range(10):
         try:
             raise Exception
         except Exception or Exception:
             pass