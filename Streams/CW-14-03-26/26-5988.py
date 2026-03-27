with open('26_5988.txt') as file:
    N = file.readline()
    boxes = sorted([i.split() for i in file], reverse = True)
print(boxes)

last_picked_box = boxes[0]
k = 1
print(last_picked_box)
# for box in boxes:
#     if int(last_picked_box[0]) - int(boxes[0]) >= 7:
#         if last_picked_box[1] != boxes[1]:
#             last_picked_box = boxes
#             k += 1
# print(k)