with open('26_5988.txt') as file:
    N = int(file.readline())
    boxes = []
    for line in file:
        size, colour = line.split()
        boxes.append([int(size), colour])

boxes.sort(reverse=True)

red_way = [max(boxes, key = lambda x: (x[1] == 'R', x))]
blue_way = [max(boxes, key = lambda x: (x[1] == 'B', x))]
green_way = [max(boxes, key = lambda x: (x[1] == 'G', x))]

for box in boxes:
    if red_way[-1][0] - box[0] >= 7 and red_way[-1][1] != box[1]:
        red_way.append(box)
    if blue_way[-1][0] - box[0] >= 7 and blue_way[-1][1] != box[1]:
        blue_way.append(box)
    if green_way[-1][0] - box[0] >= 7 and green_way[-1][1] != box[1]:
        green_way.append(box)

print(len(red_way), red_way[-1][0])
print(len(blue_way), blue_way[-1][0])
print(len(green_way), green_way[-1][0])