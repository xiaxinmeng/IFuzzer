@dataclass
class Rect:
    x: int
    y: int

r=Rect(5,2)

@dataclass
class HyperRect(Rect):
    z: int

    def __post_init__(self):
        self.vol = self.x*self.y*self.z

hr=HyperRect(5,2,3)
print("hr.vol", hr.vol)