import copy

import time


def RemoveAllThree(list):
    return [x for x in list if list.count(x) is not 3]


def RemoveAllFour(list):
    return [x for x in list if list.count(x) is not 4]


def RemoveAllNeighbor(list):
    temp = copy.deepcopy(list)
    for l in list:
        if l > 39 or l not in temp:
            continue
        if l + 1 in temp and l + 2 in temp:
            del temp[temp.index(l): temp.index(l) + 3]
        elif l - 1 in temp and l + 1 in temp:
            del temp[temp.index(l - 1): temp.index(l) + 2]
        elif l - 1 in temp and l - 2 in temp:
            del temp[temp.index(l - 2): temp.index(l) + 1]
    return temp


def start(list):
    L = []
    for e in list:
        if list.count(e) >= 2 and e not in L:
            L.append(e)
    for i in L:
        temp = copy.deepcopy(list)
        temp.remove(i)
        temp.remove(i)
        for i in range(0, 6):
            if i is 0:
                temp2 = RemoveAllThree(RemoveAllFour(RemoveAllNeighbor(temp)))
            if i is 1:
                temp2 = RemoveAllNeighbor(RemoveAllThree(RemoveAllFour(temp)))
            if i is 2:
                temp2 = RemoveAllFour(RemoveAllNeighbor(RemoveAllThree(temp)))
            if i is 3:
                temp2 = RemoveAllFour(RemoveAllThree(RemoveAllNeighbor(temp)))
            if i is 4:
                temp2 = RemoveAllThree(RemoveAllNeighbor(RemoveAllFour(temp)))
            if i is 5:
                temp2 = RemoveAllThree(RemoveAllFour(RemoveAllNeighbor(temp)))
            if len(temp2) is 0:
                return "win"
    return "can not win"


s = time.time()
print(start([11,11,11,21,21,21,22,22,31,32,33,33,33,33]))
print(time.time() - s)
