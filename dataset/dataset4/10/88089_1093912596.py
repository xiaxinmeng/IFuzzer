class VecMixin:
    def length(self):
        return math.hypot(*self)

class Vec2D(NamedTuple, VecMixin):
    x: float
    y: float

class Vec3D(NamedTuple, VecMixin):
    x: float
    y: float
    z: float