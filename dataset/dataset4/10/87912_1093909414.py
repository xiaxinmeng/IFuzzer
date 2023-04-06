
class A:
    dataclasses: dataclasses.Field = dataclasses.field()

A.dataclasses.other  # mypy error: "Field[Any]" has no attribute "other"
