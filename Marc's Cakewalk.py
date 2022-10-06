def marcsCakewalk(calorie):
    # Write your code here
    total = 0
    l = sorted(calorie, reverse = True)
    for i in range(len(calorie)):
        total += (2**i)*l[i]
    return total