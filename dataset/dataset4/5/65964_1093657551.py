for i in range(65536):
    c = chr(i)
    c2 = 'a'+c
    if is_id_char(c) != c2.isidentifier():
        print('\\u%.4x'%i,is_id_char(c),c2.isidentifier())