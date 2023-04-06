class attribute:
  def __init__(self, func):
    self.func = func
  def __get__(self, instance, owner):
    if instance is None:
      return self
    return self.func.__get__(instance, owner)