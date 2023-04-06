from functools import cached_property
from threading import Thread
from random import randint
import time



class Spam:
    @cached_property
    def ham(self):
        print(f'Calculating amount of ham in {self}')
        time.sleep(10)
        return randint(0, 100)


def bacon():
    spam = Spam()
    print(f'The amount of ham in {spam} is {spam.ham}')


start = time.time()
threads = []
for _ in range(3):
    t = Thread(target=bacon)
    threads.append(t)
    t.start()

for t in threads:
    t.join()