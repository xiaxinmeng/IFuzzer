max_recursion = 3
while '%' in userhome and max_recursion > 0:
    userhome = expandvars(userhome)
    max_recursion -= 1