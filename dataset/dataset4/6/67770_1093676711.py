while q.qsize():                                                         
    try:                                                                 
        item = q.get_nowait()                                                   
    except Empty:                                                        
        pass