from typing import NamedTuple


class MyTestedTuple(NamedTuple):
    example_text = "default_text"
    example_int: int = 3


if __name__ == '__main__':
    print(MyTestedTuple().example_text)
    fault_tuple = MyTestedTuple(example_text="text_from_call")
    print(fault_tuple.example_text)