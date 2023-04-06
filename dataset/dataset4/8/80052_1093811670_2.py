def main(nn=10):
    xx = list(range(nn))
    import pdb; pdb.set_trace()
    for ii in range(nn):
        num = sum(xx[jj] for jj in range(nn))
    print('xx', xx)

if __name__ == '__main__':
    main()