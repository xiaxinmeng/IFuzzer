from textwrap import wrap

text = ("a\tb "
        "a\tb")

lines = wrap(text, width=5, tabsize=4)
for line in lines:
    print(repr(line))