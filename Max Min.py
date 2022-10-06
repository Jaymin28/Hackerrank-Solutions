import sys

def maxMin(k, arr):
    # Write your code here
    n = len(arr)
    arr.sort()
    minuf = sys.maxsize
    for i in range(n-k+1):
        minuf = min(minuf, (arr[i+k-1] - arr[i]))
    
    return minuf