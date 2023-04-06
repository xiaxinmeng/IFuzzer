Liste   = []
StringL = ["Nr.:", "NR", "Bielefeld", "Paderborn", "Lemgo"]
for i in range (10):
    StringL[1] = str(i)
    Liste.append(StringL)
    print (StringL)
    #print (Liste)
    print ()

print()
for i in range (10):
    print (Liste[i])