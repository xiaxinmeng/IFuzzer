import traceback
try:
    try:
        raise TypeError
    except:
        try:
            raise ValueError
        except:
            raise KeyError from None
except BaseException as exc:
    e = exc

print([e, e.__cause__, e.__context__, e.__suppress_context__])
traceback.print_exception(type(e), e, e.__traceback__)