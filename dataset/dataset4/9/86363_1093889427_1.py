
def call():
    import sys
    frame = sys._getframe()
    print(frame.f_back.f_locals)
   
def main():
    a = 1
    call()
   
if __name__ == '__main__':
    main()
