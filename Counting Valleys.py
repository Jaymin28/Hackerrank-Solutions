def countingValleys(steps, path):
    # Write your code here
    pos = 0
    count = 0
    for i in range(steps):
        if path[i] == 'U':
            pos += 1
            if pos == 0:
                count += 1
        elif path[i] == 'D':
            pos -= 1
    return count