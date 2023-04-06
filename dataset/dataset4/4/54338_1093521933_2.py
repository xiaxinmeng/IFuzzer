def main():
    import sys
    exec(compile(open(sys.argv[1]).read(), sys.argv[1], 'exec'))

if __name__=='__main__':
    main()