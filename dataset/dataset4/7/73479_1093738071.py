import multiprocessing as mp

condition = mp.Condition()

with condition:
    condition.notify(2) #Docs show notify(n=1)
#TypeError: notify() takes 1 positional argument but 2 were given