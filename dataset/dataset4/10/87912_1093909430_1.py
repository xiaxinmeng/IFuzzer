
@dataclass
class A:
  datetime: datetime.Time = field(default_factory=datetime.Time.now)
