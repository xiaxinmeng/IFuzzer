
def foo():
     #image 1
     yield sys._getframe()
    #image 2

def gen():
     yield foo()

def main():
     for f in gen():
          print(f)
