def printPicnic(items, lwidth, rwidth):
    '''
    print the number and the items you need to bring to a picnic
    :param items: string
    :param lwidth: int
    :param rwidth: int
    :return: None
    '''
    print('PICNIC ITEMS'.center(lwidth + rwidth,'-'))
    for k, v in items.items():
        print(k.ljust(lwidth, '.'),str(v).rjust(rwidth))

picnic = {'sandwiches':4, 'apples':12, 'cups':4, 'cookies':8000}
printPicnic(picnic, 12, 5)
printPicnic(picnic, 20, 6)


