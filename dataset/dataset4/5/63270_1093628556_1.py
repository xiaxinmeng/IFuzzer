class Wrapper(object):
  def __init__(self, *args, **kwargs):
    self.__obj = KazooClient(*args, **kwargs)
    self.__obj.start()
  def __getattr__(self, attr):
    return getattr(self.__obj, attr)
  def __del__(self):
    self.__obj.stop()