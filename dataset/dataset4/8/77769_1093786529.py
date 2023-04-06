def func(ϵ, α, γ, ϕ):
    pass

varnames = func.__code__.co_varnames
print(varnames)
print('ϵ' == varnames[0])
print('α' == varnames[1])
print('γ' == varnames[2])
print('ϕ' == varnames[3])