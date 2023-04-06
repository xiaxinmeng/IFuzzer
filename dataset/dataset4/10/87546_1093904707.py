def demo():
    a = 1
    class B:
        x = a
    print(B.x)  # Okay.
    
    class C:
        x = a  # Fails.
        if False:
            a = None
    print(C.x)