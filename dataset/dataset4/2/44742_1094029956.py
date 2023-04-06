class myunicode(unicode):
  def __init__(self, *args, **kwargs):
    unicode.__init__(self, *args, **kwargs)
    self.someattribute = calculate_attribute_once()