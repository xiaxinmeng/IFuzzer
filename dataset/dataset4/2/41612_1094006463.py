def decode_list(x, f):                                
                         
    r, f = [], f+1                                    
                         
    while x[f] != 'e':                                
                         
        v, f = decode_func[x[f]](x, f)                
                         
        r.append(v)                                   
                         
    return (r, f + 1)