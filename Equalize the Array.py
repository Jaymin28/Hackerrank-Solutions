def equalizeArray(arr):
    # Write your code here
    from collections import Counter
    x = Counter(arr)
    ans = len(arr) - max(x.values())
    return ans