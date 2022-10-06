def gameOfThrones(s):
    # Write your code here
    from collections import Counter
    d = Counter(s)
    count = 0
    for v in d.values():
        if count > 1:
            return 'NO'
        elif v % 2 != 0:
            count += 1
    return 'YES'