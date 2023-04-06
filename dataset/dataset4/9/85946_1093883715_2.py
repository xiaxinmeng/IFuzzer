def __dir__(self):
    r = super().__dir__()
    return r + attribute_names_list + method_names_list