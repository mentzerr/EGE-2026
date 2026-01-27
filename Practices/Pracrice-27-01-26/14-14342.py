for p in range(int(max('BOOMBLCNG'), 36) + 1, 37):
    num1 = int('BO', p)
    num2 = int('OM', p)
    num3 = int('BL4', p)
    num4 = int('CNG', p)
    if num1 + num2 + num3 == num4:
        print(p)