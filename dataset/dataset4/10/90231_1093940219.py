
from ast import *

# if we build the module manually and try it directly
value = Module(
    body=[
        FunctionDef(
            name="items_needed",
            args=arguments(
                posonlyargs=[],
                args=[],
                kwonlyargs=[],
                kw_defaults=[],
                defaults=[],
            ),
            body=[Return(value=Constant(value="test"))],
            decorator_list=[],
            lineno=1,
            column=1,
        )
    ],
    type_ignores=[],
)

unparse(value)  # ok
