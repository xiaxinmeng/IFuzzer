import json
class ComplexEncoder(json.JSONEncoder):
    def default(self, obj):
        print("hi")
        if isinstance(obj, complex):
            return [obj.real, obj.imag]
        # Let the base class default method raise the TypeError
        return json.JSONEncoder.default(self, obj)

s2=json.dumps(2 + 1j, cls=ComplexEncoder)
print(s2)