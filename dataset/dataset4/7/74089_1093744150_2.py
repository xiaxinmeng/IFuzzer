s3 = Struct(s1.format_str + s2.format_str[1:])
s3 = Struct(s1.format_str + "B")  # if s2 is not needed on its own
ver2 = Struct(ver1.format_str + "I")
version_a = Struct(start.format_str + union_b.format_str[1:])