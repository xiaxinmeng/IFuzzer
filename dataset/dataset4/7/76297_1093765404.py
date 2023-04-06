def csv2list(file_name): 
    list_name=[] 
    with open(file_name) as csvfile:
        readerfile = reader(csvfile)
        for row in readerfile:
            list_name.append(row)
    return list_name

def list2csv(list_name,file_name):
    with open(file_name, 'w', newline='') as csvfile:
        writerfile = csv.writer(csvfile)
        writerfile.writerows(list_name)