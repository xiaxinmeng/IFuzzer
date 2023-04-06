with open('file', 'r+', buffering=1) as f:
    print(f.tell())                  # => 0
    print(f.readline().strip())      # we read 1 line
    print(f.tell())                  # => 9  
    print('Hello', file=f)           # we write "Hello\n"
    print(f.tell())                  # => 34