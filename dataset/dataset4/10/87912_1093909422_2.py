
@dataclasses.dataclass
class Params:
  losses: losses.LossesParams = dataclasses.field()
  dataset: dataset.DatasetParams = dataclasses.field()
