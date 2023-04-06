class Singleton(object):
  _instance = None
  @staticmethod
  def getInstance():
    if Singleton._instance is None:
      Singleton._instance = Singleton()
    return _instace