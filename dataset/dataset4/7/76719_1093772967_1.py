from multiprocessing import Process, Manager
manager=Manager()
data=manager.list([[['','','','','','','','','','','','']]])
data[0][0][0] = 5
data[0][0][1] = "5"
print(data)    