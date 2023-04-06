from ctypes import LittleEndianStructure, c_uint8, sizeof


class Point(LittleEndianStructure):
    _pack_ = 1
    _fields_ = [
        ("x", c_uint8, 4),
        ("y", c_uint8, 8),
        ("z", c_uint8, 4),
    ]

data = Point(2, 2, 2)
print(f"size of data: {sizeof(data)}")
print(f"x: {data.x}, y: {data.y}, z: {data.z}")