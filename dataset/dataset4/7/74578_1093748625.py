selected = sel.select(timeout=1)
if not selected:
    raise Exception("Child timed out: remaining input {!r}, output {!r}".format(
        input, output))
for [_, events] in selected:
    ...