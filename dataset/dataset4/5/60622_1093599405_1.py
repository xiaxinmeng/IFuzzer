class NonIterableContainer:
  def __init__(self, container, description):
    self.container = container
    self.description = description
  def __repr__(self):
    return self.description
  def __contains__(self, item):
    return item in self.container