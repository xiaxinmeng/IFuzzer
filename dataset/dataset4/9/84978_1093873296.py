class float:
    @classmethod
    def from_floatlike(cls, obj):
        return cls(PyFloat_FromDouble(PyFloat_AsDouble(obj)))