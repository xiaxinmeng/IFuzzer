def function(input_list, a='x'):
    [input_list[i].append(a) for i in range(len(input_list))]
    return input_list

list1 = [[0], [0], [0]]
list2 = [[0]] * 3