with open(r'26_4604.txt') as file:
    N = int(file.readline())
    boxes = sorted([int(i) for i in file], reverse=True)

last_picked_box = boxes[0]
k = 1

for box in boxes:
    if last_picked_box - box >= 3:
        last_picked_box = box
        k += 1

print(k, last_picked_box)
