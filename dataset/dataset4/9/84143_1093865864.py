with open('../s01_parser_eval/data/out-6976.txt') as pgn:
    pgn.seek(1008915299)
    t = None
    while True:
        if t:
            pgn.seek(t)
        pgn.readline()
        pt = t
        t = pgn.tell()
        if pt:
            if pt > t:
                print('Strange %s!', t)
                pgn.seek(t)

        print(pgn.tell())