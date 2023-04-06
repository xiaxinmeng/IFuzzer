from multiprocessing import Manager

manager = Manager()
shared_dict = manager.dict()