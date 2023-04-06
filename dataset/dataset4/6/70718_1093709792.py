def bing():
    try:
        input()
    except EOFError:
        print("Caught an EOFError")