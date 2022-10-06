def minimumAbsoluteDifference(arr):
    # Write your code here
    l = list()
    arr.sort()
    for i in range(len(arr)-1):
        x = abs(arr[i]-arr[i+1])
        l.append(x)
    return min(l)