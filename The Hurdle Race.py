def hurdleRace(k, height):
    # Write your code here
    count = 0
    for i in height:
        if k < i:
            count += (i-k)
            k = i
    return count