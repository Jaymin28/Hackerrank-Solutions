def diagonalDifference(arr):
    # Write your code here
    sum1 = 0
    sum2 = 0
    n = len(arr)
    for i in range(0,n):
        sum1 += arr[i][i]
    for j in range(0,n):
        sum2 += arr[j][n-1-j]
    return abs(sum1-sum2)