def miniMaxSum(arr):
    # Write your code here
    l = list()
    sum = 0
    for i in range(len(arr)):
        for j in range(len(arr)):
            if j == i:
                continue
            sum += arr[j]
        l.append(int(sum))
        sum = 0
    print(min(l),max(l))