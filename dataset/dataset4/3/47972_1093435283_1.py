class C():
    def __str__(self):
        raise IndexError
print(1, C(), sep='\n')