def smolInt(listToSort):
    noNegatives = [nums for nums in listToSort if nums >= 0]
    noNegatives.sort()
    noDupes = set(noNegatives)
    noDupesList = list(noDupes)

    if noDupesList == []: #empty list, smallest int therefor 1
        return 1

    smallestVal = noDupesList[0] #list is sorted, smallest value is 1st element
    if smallestVal > 1: # if 1st element is more than 1, smallest possible missing int is 1
        return 1

    for x in range(0, len(noDupesList)):
        if x == len(noDupesList)-1: #final element
            if noDupesList[x] > smallestVal + 1: # more than 1 above current smallest value in chain
                return smallestVal + 1 # so next smallest int is the smallest value + 1
            else:
                return noDupesList[x] + 1 #otherwise all ints in chain 1->2->3 etc, so next smallest is final element + 1
        if noDupesList[x] > smallestVal + 1:
            return smallestVal + 1
        smallestVal = noDupesList[x] # current element is in the chain x-1, x, x+1 etc, so it's the new smallest val

print(smolInt([]))
