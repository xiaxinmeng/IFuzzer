orig_hook = threading.excepthook
threading.excepthook = myhook

def myhook(args):
   try:
      ...
   except:
      print("too bad!")
      orig_hook(args)