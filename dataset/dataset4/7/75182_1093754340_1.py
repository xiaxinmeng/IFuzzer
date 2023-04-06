class MyNum(int):
    def __new__(cls, num, data):
        instance = super().__new__(cls, num)
        instance.data = data
        return instance

data = [MyNum(1, ['Anna']), MyNum(3, ['Paul', 'Henry']), 
        MyNum(4, ['Kate'])]

people = median_low(data).data