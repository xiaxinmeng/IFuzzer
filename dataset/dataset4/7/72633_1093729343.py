mailbox = queue.Queue()


while True:
    #print(addr_groups)


    unknown_clients=[]
    for key in yellow_page.keys():
        if yellow_page[key][0] ==None:
            unknown_clients.append(key)

    print("\n", name_groups)
    if len(unknown_clients) >0:
        print("unknown from："+str(unknown_clients))
    print(time.strftime(ISOTIMEFORMAT, time.localtime(time.time())) + '\n')