
exclude = [2, 4]

class TestClass:
    list_1 = [1, 2, 3, 4, 5]    
    list_2 = [i for i in list_1 if i not in exclude]
