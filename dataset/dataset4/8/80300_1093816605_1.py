import json
from multiprocessing import Manager
from multiprocessing.managers import DictProxy, ListProxy

manager = Manager()
shared_dict = manager.dict()