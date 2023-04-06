match_expr_ignorecase = re.compile('"', re.IGNORECASE).match('"')
print(match_expr_ignorecase)
# <re.Match object; span=(0, 1), match='"'>
assert(match_expr_ignorecase is not None) #Passes