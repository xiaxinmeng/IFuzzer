args = get_args(int | str)
import operator, functools
functools.reduce(operator.or_, args)