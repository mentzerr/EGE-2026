file = open('9_27621')

for pos, s in enumerate(file, start = 1):
    a = [int(x) for x in s.split()]
    if len(a) == len(set(a)) and max(a) - min(a) == sum(a) - (max(a) + min(a)):
        print(pos)
