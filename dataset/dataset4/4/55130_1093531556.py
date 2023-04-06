def parseinternaldate(datestr):
    return datetime.strptime(datestr, "%d-%b-%Y %H:%M:%S %z")

def formatinternaldate(dateobj):
    return dateobj.strftime("%d-%b-%Y %H:%M:%S %z")