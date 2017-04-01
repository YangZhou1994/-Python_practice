while True:
    W = input('W = ')
    if W == 'z':
        break
    F = input('K = ')
    S = input('S = ')
    P = input('P = ')

    Output = (W - F + 2*P)/S +1
    print "Size of output is %d" % Output

