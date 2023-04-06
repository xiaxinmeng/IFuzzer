str_list = ["Emma", "Jon", "", "Kelly","Eric", "", "","KXN",""]
for item in str_list:
    if len(item) == 0:
        str_list.remove(item)
print(len(str_list[-1]))