
class myfloat(float):
    def __hash__(self):
        if self != self:  # i.e., math.isnan(self)
            return object.__hash__(self)
        return super().__hash__(self)
