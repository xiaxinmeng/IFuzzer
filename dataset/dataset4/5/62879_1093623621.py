escape_tm = dict((k, repr(chr(k))[1:-1]) for k in range(32))              
escape_tm[0] = '\0'                                                            
escape_tm[7] = '\a'                                                            
escape_tm[8] = '\b'                                                            
escape_tm[11] = '\v'                                                           
escape_tm[12] = '\f'                                                           
escape_tm[ord('\\')] = '\\\\'

def escape_control(s):                                                          
    if isinstance(s, text_types):                                               
        return s.translate(escape_tm)
    else:
        return s.decode('utf-8', 'surrogateescape').translate(escape_tm).encode('utf-8', 'surrogateescape')

def unescape_control(s):                                                        
    if isinstance(s, text_types):                                               
        return s.encode('latin1', 'backslashreplace').decode('unicode_escape')
    else:                                                                       
        return s.decode('utf-8', 'surrogateescape').encode('latin1', 'backslashreplace').decode('unicode_escape').encode('utf-8', 'surrogateescape')