def test():
    cnt=0
    for x in range(3216):
        for y in range(2136):
            cnt = cnt + 1
            print("cnt="+str(cnt)+" y=" + str(y) + " x=" + str(x) )
            if cnt > 2137 : 
                break # Break only out of "for y in in range(2136)"