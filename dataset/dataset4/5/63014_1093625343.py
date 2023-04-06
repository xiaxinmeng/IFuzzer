def clean_surrogate_escapes(s):
    return s.encode('utf-8', 'surrogatepass').decode('utf-8', 'replace')