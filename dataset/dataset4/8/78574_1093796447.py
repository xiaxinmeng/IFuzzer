with gzip.GzipFile('products.json', 'w') as outfile:
        outfile.write(json.dumps(data, outfile, sort_keys=True))