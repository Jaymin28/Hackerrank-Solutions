def largestPermutation(k, arr):
    # Write your code here
    n = len(arr)
    if k == 0:
        return arr
    elif k >= n:
        return sorted(arr, reverse = True)
    
    index = {}
    for i in range(n):
        index[arr[i]] = i
    
    i = swap =  0
    while swap < k and i < n:
        if arr[i] < n-i:
            idx = index[n-i]
            arr[i], arr[idx] = arr[idx], arr[i]
            index[arr[idx]] = idx
            index[n-i] = i
            swap += 1
        i += 1
    return arr