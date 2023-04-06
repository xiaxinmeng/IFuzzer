import traceback

def foo():
  traceback.print_exc()
  foo() 
    
foo()