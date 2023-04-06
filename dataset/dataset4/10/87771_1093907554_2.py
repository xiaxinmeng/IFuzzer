
print(eval("sum(get(i) for i in range(len(l)))"), globals(), locals())
print(eval("[get(i) for i in range(len(l))]"))
print(eval("{i:get(i) for i in range(len(l))}"))
