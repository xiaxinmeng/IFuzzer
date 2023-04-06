sayac = 0
fakto = 10000000000000000000000
while True:
    if fakto % 10 == 0:
        sayac += 1
        fakto = fakto / 10
    elif fakto % 10 > 0:
        break
print(sayac)