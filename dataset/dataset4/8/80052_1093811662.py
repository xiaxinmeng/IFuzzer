def main(nn=10):
    xx = list(range(nn))
    breakpoint()
    for ii in range(nn):
        num = sum(xx[jj] for jj in range(nn))
    print(f'xx={xx}')

if __name__ == '__main__':
    main()