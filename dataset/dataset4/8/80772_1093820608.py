def fun(NT: NamedTuple, fill):
    # Complains that NamedTuple is not callable
    nt = NT(*fill)
    return nt


UserNamedTuple = Type[NamedTuple]


def fun(NT: UserNamedTuple, fill):
    # No complaints
    nt = NT(*fill)
    return nt