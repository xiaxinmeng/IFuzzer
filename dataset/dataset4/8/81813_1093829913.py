class A:
    class B:
        def __init__(self, param):
            self.param = param
        
    l = [B(i) for i in range(10)]