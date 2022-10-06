def cutTheSticks(arr):
    # Write your code here
    ans = []
    while arr:
        ans.append(len(arr))
        min_ar = min(arr)
        arr = list(map(lambda x: x - min_ar, arr))
        arr = list(filter(lambda x: x > 0, arr))
    return ans