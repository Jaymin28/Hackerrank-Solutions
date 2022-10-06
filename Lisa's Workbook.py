def workbook(n, k, arr):
    # Write your code here
    ans = 0
    page = 1
    for pr in arr:
        for i in range(1,pr+1):
            if i == page:
                ans += 1
            if i % k == 0 or i == pr:
                page += 1
    return ans