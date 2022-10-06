def findMedian(arr):
    # Write your code here
    arr.sort()
    n = len(arr)
    return arr[(n//2)]