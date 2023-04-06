class cache_struct_converter(CConverter):
    type = 'PyStructObject *'
    converter = 'cache_struct_converter'
    c_default = "NULL"