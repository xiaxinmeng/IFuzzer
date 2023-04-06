def run(module):
    print("///////////////////////////////")
    print("//", module)
    memio = module.StringIO(newline=None)
    # The C StringIO decodes newlines in write() calls, but the Python
    # implementation only does when reading.  This function forces them to
    # be decoded for testing.
    def force_decode():
        memio.seek(0)
        print("-------->", repr(memio.getvalue()))
        memio.seek(0)
        print("========>", repr(memio.read()))
    def print_newlines():
        print(repr(memio.newlines))
    print_newlines() # None
    memio.write("a\n")
    force_decode()
    print_newlines() # "\n"
    memio.write("b\r\n")
    force_decode()
    print_newlines() # ("\n", "\r\n")
    memio.write("c\rd")
    force_decode()
    print_newlines() # ("\r", "\n", "\r\n")

def main():
    import _pyio, _io
    run(_pyio)
    run(_io)

if __name__ == '__main__':
    main()