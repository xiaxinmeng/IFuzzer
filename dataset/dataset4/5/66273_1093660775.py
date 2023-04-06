def main():
    lista =[1, 4, 5 , 5, 6 , 3 ,1]
    def ins(x):
        return lista.insert(x,0)

    for idx, v in enumerate(lista):
        if v == 5:
            ins(idx)
            print(idx, lista)
        if idx > 10:
            break

if __name__ == '__main__':
	main()