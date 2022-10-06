def compareTriplets(a, b):
    # Write your code here
    x = y = 0
    for i in range(3):
        if a[i] == b[i]:
            continue
        elif a[i]>b[i]:
            x += 1
        else:
            y += 1
    return (x,y)