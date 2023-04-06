def parseTime(strTime, format = "%a %b %d %H:%M:%S"):# example: Mon Aug 7 21:08:52                        

    locale.setlocale(locale.LC_TIME, ('en_US','UTF8'))    
    format = "%Y " + format
    strTime = str(datetime.now().year) + " " +strTime

    import _strptime
    _strptime._cache_lock.acquire()
    _strptime._TimeRE_cache = _strptime.TimeRE()
    _strptime._regex_cache = {}
    _strptime._cache_lock.release()    

    tuple = strptime(strTime, format)     
    return datetime(*tuple[0:6])