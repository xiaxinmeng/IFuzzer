class Color(AutoNumberEnum):
  red
  green
  blue
  @property
  def cap_name(self):
    return self.name.upper()