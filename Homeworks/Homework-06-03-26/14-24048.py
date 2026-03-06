def convert_10(num, sys):
    num = num[::-1]
    summary = 0
    for i in range(len(num) - 1, -1, -1):
        summary += int(num[i], 36)*sys**i

    return summary

for p in range(33, 100):
    num1 = convert_10('KOT', p)
    num2 = convert_10('GOLODNI', p)
    num3 = convert_10('MEEOW', p)
    num4 = convert_10('100', p)
    num5 = 20194023088
    if num1 + num2 == num3 * num4 - num5:
        print(convert_10('PURR', p))