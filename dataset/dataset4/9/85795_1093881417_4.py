def main():

    spamm = Spamm(12, 'hello')
    print(dir(spamm))
    print(spamm._fields)
    d = dict(spamm)
    print(d)


if __name__ == '__main__':
    main()