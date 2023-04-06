with concurrent.futures.ProcessPoolExecutor(max_workers = 1) as executor:
    results = executor.submit(pd.read_csv, path)

data = results.result()