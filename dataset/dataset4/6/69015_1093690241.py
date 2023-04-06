from decimal import Decimal, ROUND_HALF_UP
def rounded(number, n):
    ''' Round the digits after the n_th decimal point by using
    decimal module in python.
    
    For example:
    2.453 is rounded by the function of deal_round(2.453, 1),
    it will return 2.5.
    2.453 is rounded by the function of deal_round(2.453, 2),
    it will return 2.45.
    '''
    val = Decimal(number)
    acc = str(n)  # n = 0.1 or 0.01 or 0.001
    return Decimal(val.quantize(Decimal(acc), rounding=ROUND_HALF_UP))

for x in np.arange(1.0, 4.01, 0.01):
    rounded_val = rounded(x, 0.1)
    print("{:}\t{:}".format(x, rounded_val))