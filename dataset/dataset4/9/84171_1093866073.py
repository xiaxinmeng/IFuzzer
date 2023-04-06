import typing

if isinstance(annotation, str):
    annotation = typing.ForwardRef(str)._evaluate(annotation)