def nSteps(n):
    prevValue = 1
    currentValue = 1

    if n <= 1:
        return currentValue
    while n > 1:
        tempValue = prevValue
        prevValue = currentValue
        currentValue = tempValue + currentValue
        n -= 1
    return(currentValue)

print(nSteps(5))
