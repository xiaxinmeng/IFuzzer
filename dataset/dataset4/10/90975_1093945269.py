
exceptions_to_suppress = []
if some_condition:
    exceptions_to_suppress.append(ValueError)

with contextlib.suppress(*exceptions_to_suppress):
    do_a_thing()
