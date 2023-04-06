class Link(str):
  print_name = None  # type: str | None

  @property
  def friendly_name(self) -> str:
    return self.print_name or self