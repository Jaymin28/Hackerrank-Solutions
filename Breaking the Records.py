def breakingRecords(scores):
    # Write your code here
    m = M = scores[0]
    x = y = 0
    for i in scores[1:]:
        if i > M:
            M = i
            x += 1
        elif i < m:
            m = i
            y += 1
    return [x, y]