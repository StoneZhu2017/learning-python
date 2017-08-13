def powersum(power,*args):
    '''Return the sum of each argument raised to specified power.'''
    total=0
    for i in args:
        total+=pow(i,power)
        print(total)
    return total
    print('total:%d',total)

powersum(2,3,4)
powersum(2,10)
