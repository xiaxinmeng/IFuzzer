class file(io.TextIOWrapper):
    'add condition matching to a stream'
    def __init__(self,stream_or_name):
        a = stream_or_name
        buffer = (a.buffer if isinstance(a, io.TextIOWrapper)
               else io.BufferedReader(io.FileIO(a, 'r')))
        super().__init__(buffer)