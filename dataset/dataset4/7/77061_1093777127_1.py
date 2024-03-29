
start = time.time()
for i in range(1000000):
    _tran = defaultdict(lambda: 'x')
    _tran.update({40: 40,    # ord('(')
                  91: 40,    # ord('[')
                  123: 40,   # ord('{')
                  41: 41,    # ord(')')
                  93: 41,    # ord(']')
                  125: 41,   # ord('}')
                  34: 34,    # ord('"')
                  39: 39,    # ord("'")
                  92: 92,    # ord("\\")
                  10: 10,    # ord("\n")
                  35: 35,    # ord("#")
                  })
end = time.time()
print(f'translate time: {end - start}')
