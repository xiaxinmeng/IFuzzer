import io
import tokenize

# picked as the second longest file in cpython
with open('Lib/test/test_socket.py', 'rb') as f:
    bio = io.BytesIO(f.read())


def main():
    for _ in range(10):
        bio.seek(0)
        for _ in tokenize.tokenize(bio.readline):
            pass

if __name__ == '__main__':
    exit(main())