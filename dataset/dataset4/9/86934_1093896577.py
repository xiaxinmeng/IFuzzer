class MyTuple(tuple):

    def __new__(cls, *items):
        print(cls, items)
        return super().__new__(cls, items)


class MyList(list):

    def __new__(cls, *items):
        print(cls, items)
        return super().__new__(cls, items)


def main():

    my_tuple = MyTuple(1, 2, 3, 'foo', 'bar')
    print('My tuple:', my_tuple)
    my_list = MyList(1, 2, 3, 'foo', 'bar')
    print('My list:', my_list)


if __name__ == '__main__':
    main()