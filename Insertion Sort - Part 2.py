def insertionSort2(n, arr):
    # Write your code here
    for a in range(1, n):
        x = arr[a]
        i = a-1
        while x < arr[i] and i >= 0:
            arr[i+1] = arr[i]
            i -= 1
        arr[i+1] = x
        print(*arr)