# more code here to keep track and store the unique elements
...
for index, i_elem in enumerate(parameters):
    is_duplicate = False
    for j_elem in parameters[index:]:
        if i_elem == j_elem:
            is_duplicate = True
            break
    ...
    # more code for logic to handle the unique elements
