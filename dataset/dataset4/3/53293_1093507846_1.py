# --install-platlib
if __name__ == '__main__':
    import os
    del os.environ['LDFLAGS']
    main()