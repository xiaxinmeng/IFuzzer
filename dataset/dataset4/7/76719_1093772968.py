from multiprocessing import Manager

manager = Manager()

data = manager.list([manager.list([manager.list(['', '', '', '', '', '', '', '', '', '', '', ''])])])

print(data[0][0])
print(data[0][0][0])
print(data[0][0][1])