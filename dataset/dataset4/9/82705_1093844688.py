p = cached_property(age)
p.__set_name__(cls, 'age3')
cls.age3 = p