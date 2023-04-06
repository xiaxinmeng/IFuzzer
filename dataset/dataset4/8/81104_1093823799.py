def __str__(self):
    return str((*self,))

# And for __repr__ function
def __repr__(self):
    return f'zip{str(self)}'