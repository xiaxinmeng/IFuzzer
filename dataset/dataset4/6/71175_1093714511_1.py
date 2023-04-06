class Color(AutoNumberEnum):
  _ignore_ = 'property'
  red
  green
  blue
  @property
  def cap_name(self):
    return self.name.upper()