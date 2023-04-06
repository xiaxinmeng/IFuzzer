import textwrap
w = 50
text = "We used the enyzme 2-succinyl-6-hydroxy-2,4-cyclohexadiene-1-carboxylate synthase."
print("Input:")
print("=" * w)
print(text)
print("=" * w)
print("Using break_long_words=True, break_on_hyphens=True")
print("=" * w)
print(textwrap.fill(text, width=w, break_long_words=True, break_on_hyphens=True))
print("=" * w)