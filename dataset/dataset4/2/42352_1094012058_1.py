r.search(r'\"o')  ## returns None (WRONG)
r.search(r'\"{o}').group()  ## returns '\\"{o}"' (CORRECT)
r.search(r'{\"o}').group()  ## returns '\\"o}' (WRONG)
r.search(r'{\"{o}}').group()  ## returns '{\\"{o}}'
(CORRECT)