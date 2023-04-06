import _testcapi

def func():
    _testcapi.pymem_buffer_overflow()

def main():
    func()

if __name__ == "__main__":
    main()