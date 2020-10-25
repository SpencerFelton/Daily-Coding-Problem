def isSolution(list, value): #find if 2 items in the list sum to the value
    possible_solutions = []
    for values in list:
        required_solution = value - values
        if values in possible_solutions:
            return True
        possible_solutions.append(required_solution)
    return False

print(isSolution([1,2,3], 6)) #false
print(isSolution([10,15,5], 20)) #true
