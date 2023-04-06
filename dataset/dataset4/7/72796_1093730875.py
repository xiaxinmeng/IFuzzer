import sys

def main():
    foo = 123
    s = """if 1:
        x = foo
        x = 555
    """
    exec_script(s)

if __name__ == '__main__':
    if '--debug' in sys.argv[1:]:
        import pdb
        exec_script = pdb.exec_script
        pdb.Pdb(skip=['pdb']).set_trace()
    else:
        exec_script = exec

    main()