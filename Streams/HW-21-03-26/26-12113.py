with open('26_12113.txt') as file:
    N = file.readline()
    boxes = sorted([int(x) for x in file], reverse=True)

red_way = [max(boxes, key = lambda x: (x % 2 == 1, x))]
blue_way = [max(boxes, key = lambda x: (x % 2 == 0, x))]

for box in boxes:
    if red_way[-1] % 2 != box % 2 and red_way[-1] - box >= 7:
        red_way.append(box)
    if blue_way[-1] % 2 != box % 2 and blue_way[-1] - box >= 7:
        blue_way.append(box)

print(len(red_way), red_way[-1])
print(len(blue_way), blue_way[-1])