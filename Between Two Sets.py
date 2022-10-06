def getTotalX(a, b):
    # Write your code here
    maxA = max(a)
    minB = min(b)
    count = 0
    for i in range(maxA, minB + 1):
        flag = True
        for j in a:
            if i%j != 0:
                flag = False
                break
        if flag:
            for k in b:
                if k%i != 0:
                    flag = False
                    break
            if flag:
                count += 1
    return count