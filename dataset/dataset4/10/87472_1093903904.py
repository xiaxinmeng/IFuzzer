
import multiprocessing
multiprocessing.set_start_method("spawn")
# bootstraping only problem with spawn

def task():
    print("task")

if __name__ == "__main__":
    with multiprocessing.Pool() as p:
        p.apply(task)
else:
    raise Exception("raise in child during bootstraping phase")
    
#################################################
# or
#################################################
    
import multiprocessing
# multiprocessing.set_start_method("fork")
# fork or spawn doesn't matter

def task():
    print("task")

def init():
    raise Exception("raise in child during initialization function")

if __name__ == "__main__":
    with multiprocessing.Pool(initializer=init) as p:
        p.apply(task)
