from ctypes import POINTER, c_char, sizeof, Structure


class char_from_c(c_char):
    pass


print("Size of c_char vs size of char_from_c:")
print(sizeof(c_char))
print(sizeof(char_from_c))


class my_structure(Structure):
    _fields_ = [
        ("first_char", char_from_c),
        ("second_char", char_from_c),
        ("third_char", char_from_c),
    ]