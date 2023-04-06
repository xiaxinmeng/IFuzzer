import re

def subst(text):
   text = re.sub(r"\bnine\b", "niner", text, re.IGNORECASE)
   return text

print(subst("nine nine nine nine"))