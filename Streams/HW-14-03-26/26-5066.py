with open('26_5066.txt') as file:
    N = int(file.readline())
    containers = sorted([int(x) for x in file], reverse=True)

cell = []
while containers:
    block = []
    for container in containers:
        if len(block) == 0 or block[-1] - container >= 7:
            block.append(container)
            containers.remove(container)
    cell.append(len(block))
print(len(cell), max(cell))

##############################################################################

# while containers:
#     block = [containers[0]]
#     containers.remove(containers[0])
#     for container in containers:
#         if block[-1] - container >= 7:
#             block += [container]
#             containers.remove(container)
#     cell += [len(block)]
#
# print(len(cell), max(cell))



