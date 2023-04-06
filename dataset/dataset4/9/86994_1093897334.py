def generate_input():
    while True:
        str = input().strip()
        yield helloworld_pb2.Operazione(operazione = str)