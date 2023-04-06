def main():
    d = {'__name__': '__main__'}
    exec(compile(open(sys.argv[1]).read(), sys.argv[1], 'exec'), d)