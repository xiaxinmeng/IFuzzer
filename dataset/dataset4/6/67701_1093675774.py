class Thing(object):
  class Result(object):
    def __init__(self, something):
      self.something = something

  def worker(self):
    return self.Result(1)

  def master(self):
    pool.apply_async(self.worker)