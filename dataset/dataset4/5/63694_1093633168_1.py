with elapsed(lambda t0, t1: print(f'read_excel: {t1 - t0:.2f} s')):
    # very large spreadsheet
    df = pandas.read_excel(filename, dtype=str)