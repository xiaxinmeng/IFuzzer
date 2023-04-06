class ImportantMixin:
    def __init__(self):
        super().__init__()
        important_task()

@dataclass
class NaiveDClass(ImportantMixin):
  data1 = int
  data2 = int