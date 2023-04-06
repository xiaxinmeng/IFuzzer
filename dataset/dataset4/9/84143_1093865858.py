with open('../s01_parser_eval/data/out-6976.txt') as pgn:
    pgn.seek(1008915299)
    while True:
        pgn.readline()
        print(pgn.tell())