def missingNumbers(arr, brr):
    # Write your code here
    from collections import Counter
    c1 = Counter(arr)
    c2 = Counter(brr)
    c = c2 - c1
    return sorted(c.keys())