def multiplyList(list):
    listCopy = [1 for x in range(0, len(list))]
    for x in range(0, len(list)):
        for y in range(0, len(list)):
            if x != y:
                listCopy[x] *= list[y]
    return listCopy

print(multiplyList([3,2,1]))
