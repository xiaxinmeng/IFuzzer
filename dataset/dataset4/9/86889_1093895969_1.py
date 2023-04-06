dict = {}
for sub_dict in super_dict.values():
    dict = { **dict, **sub_dict }