class Result(object):
    def __init__(self, something):
      self.something = something

def call_work_since_can_not_be_called_normally_by_multiprocessing_from_class(self):
  result = self.worker()
  return result

class Thing(object):
  def worker(self):
    return Result(1) # how to overload it??? - no more inheritance

  def master(self):
    ...
    pool.apply_async(worker, args=(self,))