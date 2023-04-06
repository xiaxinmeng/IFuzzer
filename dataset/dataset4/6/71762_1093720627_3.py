def efficient_intersection(smaller_dict_or_set, bigger_dict_or_set):
    if len(bigger_dict_or_set) < len(smaller_dict_or_set):
        bigger_dict_or_set, smaller_dict_or_set = smaller_dict_or_set, bigger_dict_or_set
    
    return {item for item in smaller_dict_or_set if item in bigger_dict_or_set}