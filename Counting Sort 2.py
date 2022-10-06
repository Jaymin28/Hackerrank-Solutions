def countingSort(arr):
    # Write your code here
    values = [0]* 100
    ans = []
    for i in arr:
        values[i] += 1
    for i in range(len(values)):
        if values[i] > 0:
            for j in range(values[i]):
                ans.append(i)
    
    return ans