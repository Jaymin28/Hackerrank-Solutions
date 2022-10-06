def closestNumbers(arr):
    # Write your code here
    diff = 2**31
    arr.sort()
    l = []
    for i in range(1,len(arr)):
        x = arr[i] - arr[i-1]
        if x <= diff:
            if x < diff:
                diff = x
                l = []
            l.append(arr[i-1])
            l.append(arr[i])
    
    return l