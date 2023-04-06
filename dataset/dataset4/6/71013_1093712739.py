# Input is a BufferedReader and may hold extra buffered data
with open("data", "rb") as input, open("output", "wb") as output:
    header = input.read(100)  # Actually reads more bytes from OS
    process_header(header)
    copyfileobj(input, output)  # Copy starting from offset 100