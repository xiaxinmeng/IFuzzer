from testfixtures import Comparison as C

class AClass:
    def __init__(self,x,y=None):
        self.x = x
        if y:
            self.y = y
    def __repr__(self):
        return '<'+self.__class__.__name__+'>'