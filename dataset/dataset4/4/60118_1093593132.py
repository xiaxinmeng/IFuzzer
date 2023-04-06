import multiprocessing
manager = multiprocessing.Manager()
namespace = manager.Namespace()
print("create.py complete")