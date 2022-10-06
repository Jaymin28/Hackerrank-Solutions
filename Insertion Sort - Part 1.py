def insertionSort1(n, arr):
    # Write your code here
    x = arr[-1]
    i = n-2
    while x < arr[i] and i >= 0:
        arr[i+1] = arr[i]
        print(*arr)
        i -= 1
    arr[i+1] = x
    print(*arr)