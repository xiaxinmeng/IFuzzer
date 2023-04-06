import dataclasses
import typing
A = dataclasses.make_dataclass('A', ['a_var'])
typing.get_type_hints(A)  # This currently crashes