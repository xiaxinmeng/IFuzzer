class Letter(str):
    def __new__(cls, letter):
        if letter == 'EPS':
            return str.__new__(cls)
        return str.__new__(cls, letter)
    def __str__(self):
        if not self:
            return 'EPS'
        return self
w = Letter('w')
print(w)
