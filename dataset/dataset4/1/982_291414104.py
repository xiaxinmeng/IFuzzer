if TYPE_CHECKING:
    import expensive_mod
 
def fun(arg: 'expensive_mod.some_type') -> None:
    local_var: expensive_mod.another_type = other_fun()