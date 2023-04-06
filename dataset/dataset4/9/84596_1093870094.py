with open('udhr-gb2312.txt', encoding='GB2312') as f: 
    while True: 
       line = f.readline() 
       t = f.tell()
       if not line: 
           break 