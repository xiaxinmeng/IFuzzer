# fail.py
def main():
    patch = './a'
    f = open(patch, 'r')
    a = getattr(f,'encoding','ascii')
    print(str(a))

if __name__ == "__main__":
    main()