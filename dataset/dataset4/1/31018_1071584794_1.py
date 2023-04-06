Module(
    body=[
        Expr(
            value=Subscript(
                value=Name(id='l', ctx=Load()),
                slice=Tuple(
                    elts=[
                        Starred(
                            value=Name(id='Ts', ctx=Load()),
                            ctx=Load()
                        )
                    ],
                    ctx=Load()
                ),
                ctx=Load()
            )
        )
    ],
    type_ignores=[]
)